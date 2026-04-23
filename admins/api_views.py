import json

import hmac
import hashlib
import time
from django.conf import settings


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password

from admins.models import AdminUser
from members.models import Member, FedapayPaymentAttempt
from admins.utils import log_activity
from members.constants import (
    
    ADMIN_STATUS_ACTIVE,
    ADMIN_STATUS_SUSPENDED,
    
)
from members.payment_services import process_fedapay_webhook
from members.services import create_member_record


def cors_json_response(data, status=200):
    return JsonResponse(data, status=status)


def api_login(request):
    if request.method == 'OPTIONS':
        return cors_json_response({'success': True})

    if request.method != 'POST':
        return cors_json_response({
            'success': False,
            'message': 'Méthode non autorisée'
        }, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return cors_json_response({
            'success': False,
            'message': 'JSON invalide'
        }, status=400)

    email = (data.get('email') or '').strip().lower()
    password = data.get('password') or ''

    if not email or not password:
        return cors_json_response({
            'success': False,
            'message': 'Email et mot de passe obligatoires'
        }, status=400)

    try:
        user = AdminUser.objects.get(email=email)

        if user.is_locked:
            return cors_json_response({
                'success': False,
                'message': 'Compte admin bloqué ❌'
            }, status=403)

        if user.status == ADMIN_STATUS_SUSPENDED:
            return cors_json_response({
                'success': False,
                'message': 'Compte suspendu ❌'
            }, status=403)

        if user.status != ADMIN_STATUS_ACTIVE:
            return cors_json_response({
                'success': False,
                'message': 'Compte inactif ❌'
            }, status=403)

        if not check_password(password, user.password):
            user.failed_login_attempts += 1

            if user.failed_login_attempts >= 5:
                user.is_locked = True
                user.save(update_fields=['failed_login_attempts', 'is_locked', 'updated_at'])
                return cors_json_response({
                    'success': False,
                    'message': 'Compte admin bloqué après plusieurs tentatives ❌'
                }, status=403)

            user.save(update_fields=['failed_login_attempts', 'updated_at'])
            remaining = 5 - user.failed_login_attempts

            return cors_json_response({
                'success': False,
                'message': f'Mot de passe incorrect ❌ Il reste {remaining} tentative(s).'
            }, status=401)

        user.failed_login_attempts = 0
        user.save(update_fields=['failed_login_attempts', 'updated_at'])

        request.session['admin_id'] = user.id
        request.session['admin_role'] = user.role
        request.session['admin_email'] = user.email

        log_activity(
            admin_user=user,
            action='login',
            target_type='admin',
            target_id=user.id,
            details=f"{user.email} s’est connecté via mobile"
        )

        return cors_json_response({
            'success': True,
            'message': 'Connexion réussie ✅',
            'must_change_password': user.must_change_password,
            'admin': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': user.phone,
                'role': user.role,
                'status': user.status,
            }
        })

    except AdminUser.DoesNotExist:
        return cors_json_response({
            'success': False,
            'message': 'Utilisateur introuvable ❌'
        }, status=404)


def api_change_admin_password(request):
    if request.method == 'OPTIONS':
        return cors_json_response({'success': True})

    if request.method != 'POST':
        return cors_json_response({
            'success': False,
            'message': 'Méthode non autorisée'
        }, status=405)

    admin_id = request.session.get('admin_id')
    if not admin_id:
        return cors_json_response({
            'success': False,
            'message': 'Admin non authentifié'
        }, status=401)

    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return cors_json_response({
            'success': False,
            'message': 'Admin introuvable'
        }, status=404)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return cors_json_response({
            'success': False,
            'message': 'JSON invalide'
        }, status=400)

    new_password = data.get('new_password')
    confirm_password = data.get('confirm_password')

    if not new_password or not confirm_password:
        return cors_json_response({
            'success': False,
            'message': 'Les deux champs sont obligatoires'
        }, status=400)

    if len(new_password) < 6:
        return cors_json_response({
            'success': False,
            'message': 'Le mot de passe doit contenir au moins 6 caractères'
        }, status=400)

    if new_password != confirm_password:
        return cors_json_response({
            'success': False,
            'message': 'Les deux mots de passe ne correspondent pas'
        }, status=400)

    admin.password = make_password(new_password)
    admin.must_change_password = False
    admin.save(update_fields=['password', 'must_change_password', 'updated_at'])

    log_activity(
        admin_user=admin,
        action='change_admin_password',
        target_type='admin',
        target_id=admin.id,
        details=f"{admin.email} a changé son mot de passe via mobile"
    )

    return cors_json_response({
        'success': True,
        'message': 'Mot de passe changé avec succès ✅'
    })


def api_create_member(request):
    if request.method == 'OPTIONS':
        return cors_json_response({'success': True})

    if request.method != 'POST':
        return cors_json_response({
            'success': False,
            'message': 'Méthode non autorisée'
        }, status=405)

    admin_id = request.session.get('admin_id')
    if not admin_id:
        return cors_json_response({
            'success': False,
            'message': 'Admin non authentifié'
        }, status=401)

    try:
        current_admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return cors_json_response({
            'success': False,
            'message': 'Admin introuvable'
        }, status=404)

    signature = request.FILES.get('signature')
    if signature and not signature.name.lower().endswith('.png'):
        return cors_json_response({
            'success': False,
            'message': 'La signature doit être en format PNG'
        }, status=400)

    try:
        member = create_member_record(request.POST, request.FILES, current_admin)
    except ValueError as e:
        return cors_json_response({
            'success': False,
            'message': str(e)
        }, status=400)
    except Exception:
        return cors_json_response({
            'success': False,
            'message': 'Erreur serveur'
        }, status=500)

    log_activity(
        admin_user=current_admin,
        action='create_member',
        target_type='member',
        target_id=member.id,
        details=f"{current_admin.email} a créé le membre {member.nim}"
    )

    return cors_json_response({
        'success': True,
        'message': 'Membre enregistré avec succès ✅',
        'member': {
            'id': member.id,
            'nim': member.nim,
            'first_name': member.first_name,
            'last_name': member.last_name,
            'phone': member.phone,
            'id_card_type': member.id_card_type,
            'status': member.status,
            'created_at': member.created_at.isoformat(),
        }
    }, status=201)


def api_member_history(request):
    if request.method == 'OPTIONS':
        return cors_json_response({'success': True})

    if request.method != 'GET':
        return cors_json_response({
            'success': False,
            'message': 'Méthode non autorisée'
        }, status=405)

    admin_id = request.session.get('admin_id')
    if not admin_id:
        return cors_json_response({
            'success': False,
            'message': 'Admin non authentifié'
        }, status=401)

    try:
        members = Member.objects.filter(
            created_by_id=admin_id
        ).order_by('-created_at')

        members_data = []
        for member in members:
            members_data.append({
                'id': member.id,
                'nim': member.nim,
                'first_name': member.first_name,
                'last_name': member.last_name,
                'phone': member.phone or '',
                'created_at': member.created_at.isoformat(),
            })

        return cors_json_response({
            'success': True,
            'members': members_data,
        })

    except Exception:
        return cors_json_response({
            'success': False,
            'message': 'Erreur serveur'
        }, status=500)


def api_get_member_by_nim(request):
    if request.method == 'OPTIONS':
        return cors_json_response({'success': True})

    if request.method != 'GET':
        return cors_json_response({
            'success': False,
            'message': 'Méthode non autorisée'
        }, status=405)

    admin_id = request.session.get('admin_id')
    if not admin_id:
        return cors_json_response({
            'success': False,
            'message': 'Non authentifié'
        }, status=401)

    nim = (request.GET.get('nim') or '').strip()

    if not nim:
        return cors_json_response({
            'success': False,
            'message': 'NIM manquant'
        }, status=400)

    try:
        member = Member.objects.get(nim=nim)
        return cors_json_response({
            'success': True,
            'member': {
                'nim': member.nim,
                'first_name': member.first_name,
                'last_name': member.last_name,
                'phone': member.phone or '',
            }
        })
    except Member.DoesNotExist:
        return cors_json_response({
            'success': False,
            'message': 'Membre introuvable'
        }, status=404)


def verify_fedapay_signature(raw_body: bytes, signature_header: str) -> bool:
    """
    Vérifie la signature du webhook FedaPay.

    IMPORTANT :
    - FedaPay documente l'usage de X-FEDAPAY-SIGNATURE + secret webhook + body brut.
    - La doc publique consultée ne donne pas clairement l'algorithme Python exact.
    - Cette implémentation suppose un format de type : t=TIMESTAMP,v1=SIGNATURE_HEX
      avec une signature HMAC SHA256 sur "timestamp.payload".
    - À valider une fois avec un vrai webhook FedaPay sandbox.
    """
    secret = settings.FEDAPAY_WEBHOOK_SECRET
    if not secret:
        return False

    if not signature_header:
        return False

    parts = {}
    for item in signature_header.split(','):
        if '=' in item:
            k, v = item.split('=', 1)
            parts[k.strip()] = v.strip()

    timestamp = parts.get('t')
    received_signature = parts.get('v1')

    if not timestamp or not received_signature:
        return False

    try:
        ts = int(timestamp)
    except ValueError:
        return False

    # Rejette les signatures trop anciennes (5 min)
    now = int(time.time())
    if abs(now - ts) > 300:
        return False

    signed_payload = f"{timestamp}.".encode("utf-8") + raw_body
    expected_signature = hmac.new(
        secret.encode("utf-8"),
        signed_payload,
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(expected_signature, received_signature)


@csrf_exempt
def fedapay_webhook(request):
    if request.method != 'POST':
        return cors_json_response({
            'success': False,
            'message': 'Méthode non autorisée'
        }, status=405)

    content_type = request.headers.get('Content-Type', '')
    if 'application/json' not in content_type:
        return cors_json_response({
            'success': False,
            'message': 'Content-Type invalide'
        }, status=400)

    signature = request.headers.get('X-FEDAPAY-SIGNATURE', '')
    if not signature:
        return cors_json_response({
            'success': False,
            'message': 'Signature webhook manquante'
        }, status=400)

    raw_body = request.body

    try:
        if not verify_fedapay_signature(raw_body, signature):
            return cors_json_response({
                'success': False,
                'message': 'Signature webhook invalide'
            }, status=400)
    except Exception:
        return cors_json_response({
            'success': False,
            'message': 'Erreur vérification signature'
        }, status=400)

    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError:
        return cors_json_response({
            'success': False,
            'message': 'JSON invalide'
        }, status=400)

    event_name = payload.get('name') or payload.get('event')
    allowed_events = {
        'transaction.approved',
        'transaction.declined',
        'transaction.created',
        'transaction.canceled',
        'transaction.cancelled',
    }

    if event_name and event_name not in allowed_events:
        return cors_json_response({
            'success': True,
            'message': 'Événement ignoré'
        })

    try:
        result = process_fedapay_webhook(payload)

        messages = {
            'declined': 'Paiement refusé',
            'pending': 'Paiement en attente',
            'already_processed': 'Paiement déjà enregistré',
            'approved': 'Paiement confirmé et enregistré',
        }

        return cors_json_response({
            'success': True,
            'message': messages.get(result, 'Traitement terminé')
        })

    except FedapayPaymentAttempt.DoesNotExist:
        return cors_json_response({
            'success': False,
            'message': 'Tentative de paiement introuvable'
        }, status=404)

    except Exception:
        return cors_json_response({
            'success': False,
            'message': 'Erreur webhook'
        }, status=500)