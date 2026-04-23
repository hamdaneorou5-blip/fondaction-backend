import json

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

    try:
        payload = json.loads(request.body)
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





from functools import wraps
from django.http import HttpResponse
from django.shortcuts import redirect


def admin_session_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('admin_id'):
            return redirect('/admins/login/')
        return view_func(request, *args, **kwargs)
    return wrapper


def super_admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('admin_id'):
            return redirect('/admins/login/')
        if request.session.get('admin_role') != 'super_admin':
            return HttpResponse("Accès refusé ❌")
        return view_func(request, *args, **kwargs)
    return wrapper


def member_session_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('member_id'):
            return redirect('/admins/member-login/')
        return view_func(request, *args, **kwargs)
    return wrapper





from django.db import models


class AdminUser(models.Model):
    ROLE_CHOICES = [
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
    ]

    STATUS_CHOICES = [
        ('active', 'Actif'),
        ('suspended', 'Suspendu'),
        ('inactive', 'Inactif'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    nim = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='admin')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active')
    must_change_password = models.BooleanField(default=False)
    failed_login_attempts = models.PositiveIntegerField(default=0)
    is_locked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email




from django.urls import path

from .web_views import (
    home,
    login,
    change_admin_password,
    dashboard,
    members_hub,
    admins_hub,
    admin_list,
    create_admin,
    admin_detail,
    reset_admin_password,
    admin_performance_detail,
    export_admin_performance_excel,
    suspend_admin,
    reactivate_admin,
    activity_logs,
    create_member,
    member_list,
    member_detail,
    member_login,
    member_space,
    member_logout,
    logout,
    reset_member_pin,
    member_change_pin,
    member_card,
    download_member_card_pdf,
    edit_member,
    suspend_member,
    activate_member,
    member_creation_history,
    export_members_excel,
    export_admins_excel,
    member_payment,
    start_member_payment,
    payment_return,
    member_transactions,
    info_post_list,
    create_info_post,
    member_info_posts,
    edit_info_post,
    delete_info_post,
    member_profile,
    member_settings,
    member_withdrawal,
    withdrawal_requests,
    approve_withdrawal,
    reject_withdrawal,
    member_transaction_detail,
    search_transactions,
    member_assistance,

)

from .api_views import (
    api_login,
    api_change_admin_password,
    api_create_member,
    api_member_history,
    api_get_member_by_nim,
    fedapay_webhook,

)

urlpatterns = [
    path('', home),
    path('login/', login),
    path('logout/', logout),
    path('dashboard/', dashboard),
    path('members-hub/', members_hub),
    path('admins-hub/', admins_hub),

    path('list/', admin_list),
    path('create/', create_admin),
    path('api/member-by-nim/', api_get_member_by_nim, name='api_member_by_nim'),
    path('change-password/', change_admin_password),

    path('admins/<int:admin_id>/', admin_detail),
    path('admins/<int:admin_id>/reset-password/', reset_admin_password),
    path('admins/<int:admin_id>/performance/', admin_performance_detail),
    path('admins/<int:admin_id>/performance/export/', export_admin_performance_excel),

    path('suspend/<int:admin_id>/', suspend_admin),
    path('reactivate/<int:admin_id>/', reactivate_admin),

    path('logs/', activity_logs),

    path('members/', member_list),
    path('members/create/', create_member),
    path('members/<int:member_id>/', member_detail),
    path('members/<int:member_id>/edit/', edit_member),
    path('members/<int:member_id>/suspend/', suspend_member),
    path('members/<int:member_id>/activate/', activate_member),
    path('members/<int:member_id>/reset-pin/', reset_member_pin),
    path('members/history/', member_creation_history),
    path('members/export/', export_members_excel),

    path('admins/export/', export_admins_excel),

    path('member-login/', member_login),
    path('member-space/', member_space),
    path('member-logout/', member_logout),
    path('member-change-pin/', member_change_pin),
    path('member-card/', member_card),
    path('member-card/download-pdf/', download_member_card_pdf),
    path('member-payment/', member_payment),
    path('member-payment/start/', start_member_payment),
    path('payment-return/', payment_return),
    path('member-transactions/', member_transactions),

    path('api/login/', api_login, name='api_login'),
    path('api/change-password/', api_change_admin_password, name='api_change_admin_password'),
    path('api/members/create/', api_create_member, name='api_create_member'),
    path('api/members/history/', api_member_history, name='api_member_history'),
    path('api/fedapay/webhook/', fedapay_webhook, name='fedapay_webhook'),
    path('info-posts/', info_post_list),
    path('info-posts/create/', create_info_post),
    path('info-posts/<int:post_id>/edit/', edit_info_post),
    path('info-posts/<int:post_id>/delete/', delete_info_post),
    path('member-infos/', member_info_posts),
    path('member-profile/', member_profile),
    path('member-settings/', member_settings),
    path('member-withdrawal/', member_withdrawal),
    path('withdrawal-requests/', withdrawal_requests),
    path('withdrawal-requests/<int:withdrawal_id>/approve/', approve_withdrawal),
    path('withdrawal-requests/<int:withdrawal_id>/reject/', reject_withdrawal),
    path('member-transaction/<int:transaction_id>/', member_transaction_detail),
    path('search-transactions/', search_transactions),
    path('member-assistance/', member_assistance),

]



import secrets
import string

from logs.models import ActivityLog


def log_activity(admin_user, action, target_type=None, target_id=None, details=None, status='success'):
    ActivityLog.objects.create(
        admin_user=admin_user,
        action=action,
        target_type=target_type,
        target_id=target_id,
        details=details,
        status=status
    )


def generate_temporary_password(length=12):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def generate_temporary_pin(length=5):
    digits = string.digits
    return ''.join(secrets.choice(digits) for _ in range(length))





import openpyxl
from io import BytesIO
from datetime import timedelta


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from django.template.loader import get_template
from django.utils import timezone
from xhtml2pdf import pisa
from members.models import InfoPost
from django.utils import timezone
from django.shortcuts import get_object_or_404
from admins.models import AdminUser
from members.models import Member, MemberTransaction, WithdrawalRequest
from admins.utils import (
    log_activity,
    generate_temporary_password,
    generate_temporary_pin,
)
from admins.decorators import (
    admin_session_required,
    super_admin_required,
    member_session_required,
)


from members.services import (
    get_total_contributions,
    get_available_balance,
    get_recent_transactions,
    create_withdrawal_request,
    approve_withdrawal_request,
    reject_withdrawal_request,
)


from members.permissions import forbid_if_no_member_access
from members.constants import (
    DEFAULT_MONTHLY_CONTRIBUTION,
    DEFAULT_PAYMENT_MONTHS,
    MEMBER_STATUS_ACTIVE,
    MEMBER_STATUS_SUSPENDED,
    ADMIN_STATUS_ACTIVE,
    ADMIN_STATUS_SUSPENDED,
    MAX_MEMBER_PIN_ATTEMPTS,
)
from members.payment_services import start_fedapay_payment
from members.services import create_member_record, validate_uploaded_image


def home(request):
    if request.session.get('admin_id'):
        return redirect('/admins/dashboard/')

    if request.session.get('member_id'):
        return redirect('/admins/member-space/')

    return redirect('/admins/login/')


def login(request):
    if request.method == 'POST':
        email = (request.POST.get('email') or '').strip().lower()
        password = request.POST.get('password') or ''

        try:
            user = AdminUser.objects.get(email=email)

            if user.is_locked:
                return HttpResponse("Compte admin bloqué ❌")

            if user.status == ADMIN_STATUS_SUSPENDED:
                return HttpResponse("Compte suspendu ❌")

            if user.status != ADMIN_STATUS_ACTIVE:
                return HttpResponse("Compte inactif ❌")

            if not check_password(password, user.password):
                user.failed_login_attempts += 1

                if user.failed_login_attempts >= 5:
                    user.is_locked = True
                    user.save(update_fields=['failed_login_attempts', 'is_locked', 'updated_at'])
                    return HttpResponse("Compte admin bloqué après plusieurs tentatives ❌")

                user.save(update_fields=['failed_login_attempts', 'updated_at'])
                remaining = 5 - user.failed_login_attempts
                return HttpResponse(f"Mot de passe incorrect ❌ Il reste {remaining} tentative(s).")

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
                details=f"{user.email} s’est connecté"
            )

            if user.must_change_password:
                return redirect('/admins/change-password/')

            return redirect('/admins/dashboard/')

        except AdminUser.DoesNotExist:
            return HttpResponse("Utilisateur introuvable ❌")

    return render(request, 'admins/login.html')


@admin_session_required
def logout(request):
    request.session.flush()
    return redirect('/admins/login/')


@admin_session_required
def change_admin_password(request):
    try:
        admin = AdminUser.objects.get(id=request.session.get('admin_id'))
    except AdminUser.DoesNotExist:
        request.session.flush()
        return redirect('/admins/login/')

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not new_password or len(new_password) < 6:
            return HttpResponse("Le nouveau mot de passe doit contenir au moins 6 caractères ❌")

        if new_password != confirm_password:
            return HttpResponse("Les deux mots de passe ne correspondent pas ❌")

        admin.password = make_password(new_password)
        admin.must_change_password = False
        admin.save(update_fields=['password', 'must_change_password', 'updated_at'])

        log_activity(
            admin_user=admin,
            action='change_admin_password',
            target_type='admin',
            target_id=admin.id,
            details=f"{admin.email} a changé son mot de passe"
        )

        return redirect('/admins/dashboard/')

    return render(request, 'admins/admin_change_password.html', {
        'admin': admin
    })


@admin_session_required
def dashboard(request):
    admin_id = request.session.get('admin_id')
    admin_email = request.session.get('admin_email')
    role = request.session.get('admin_role')

    total_members = Member.objects.count()
    total_admins = AdminUser.objects.count()

    today = timezone.localdate()
    start_of_week = today - timedelta(days=today.weekday())
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)

    global_today = Member.objects.filter(created_at__date=today).count()
    global_this_week = Member.objects.filter(created_at__date__gte=start_of_week).count()
    global_this_month = Member.objects.filter(created_at__date__gte=start_of_month).count()
    global_this_year = Member.objects.filter(created_at__date__gte=start_of_year).count()

    admin_today = Member.objects.filter(created_by_id=admin_id, created_at__date=today).count()
    admin_this_week = Member.objects.filter(created_by_id=admin_id, created_at__date__gte=start_of_week).count()
    admin_this_month = Member.objects.filter(created_by_id=admin_id, created_at__date__gte=start_of_month).count()
    admin_this_year = Member.objects.filter(created_by_id=admin_id, created_at__date__gte=start_of_year).count()

    return render(request, 'admins/dashboard.html', {
        'email': admin_email,
        'role': role,
        'total_members': total_members,
        'total_admins': total_admins,
        'global_today': global_today,
        'global_this_week': global_this_week,
        'global_this_month': global_this_month,
        'global_this_year': global_this_year,
        'admin_today': admin_today,
        'admin_this_week': admin_this_week,
        'admin_this_month': admin_this_month,
        'admin_this_year': admin_this_year,
    })


@admin_session_required
def members_hub(request):
    return render(request, 'admins/members_hub.html')


@admin_session_required
def admins_hub(request):
    return render(request, 'admins/admins_hub.html')


@admin_session_required
def create_info_post(request):
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        content = (request.POST.get('content') or '').strip()
        video_url = (request.POST.get('video_url') or '').strip() or None
        image = request.FILES.get('image')

        if not title or not content:
            return HttpResponse("Titre et contenu obligatoires ❌")

        admin = AdminUser.objects.get(id=request.session.get('admin_id'))

        InfoPost.objects.create(
            title=title,
            content=content,
            video_url=video_url,
            image=image,
            is_published=True,
            published_at=timezone.now(),
            created_by=admin
        )

        return redirect('/admins/info-posts/')

    return render(request, 'admins/create_info_post.html')


@admin_session_required
def info_post_list(request):
    posts = InfoPost.objects.all().order_by('-created_at')

    return render(request, 'admins/info_post_list.html', {
        'posts': posts
    })



@admin_session_required
def edit_info_post(request, post_id):
    try:
        post = InfoPost.objects.get(id=post_id)
    except InfoPost.DoesNotExist:
        return HttpResponse("Post introuvable ❌")

    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        content = (request.POST.get('content') or '').strip()
        video_url = (request.POST.get('video_url') or '').strip() or None
        image = request.FILES.get('image')

        if not title or not content:
            return HttpResponse("Titre et contenu obligatoires ❌")

        post.title = title
        post.content = content
        post.video_url = video_url

        if image:
            post.image = image

        if not post.published_at:
            post.published_at = timezone.now()

        post.save()

        return redirect('/admins/info-posts/')

    return render(request, 'admins/edit_info_post.html', {
        'post': post
    })


@admin_session_required
def delete_info_post(request, post_id):
    if request.method != 'POST':
        return redirect('/admins/info-posts/')

    try:
        post = InfoPost.objects.get(id=post_id)
    except InfoPost.DoesNotExist:
        return HttpResponse("Post introuvable ❌")

    post.delete()
    return redirect('/admins/info-posts/')    


def member_info_posts(request):
    member_id = request.session.get('member_id')
    if not member_id:
        return redirect('/admins/member-login/')

    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    posts = InfoPost.objects.filter(is_published=True).order_by('-published_at', '-created_at')

    return render(request, 'admins/member_info_posts.html', {
        'member': member,
        'posts': posts
    })



@super_admin_required
def admin_list(request):
    admins = AdminUser.objects.all().order_by('-created_at')
    return render(request, 'admins/admin_list.html', {
        'admins': admins
    })


@super_admin_required
def create_admin(request):
    if request.method == 'POST':
        nim = (request.POST.get('nim') or '').strip()
        email = (request.POST.get('email') or '').strip().lower()
        role = (request.POST.get('role') or '').strip()

        if not nim:
            return HttpResponse("Le NIM est obligatoire ❌")

        if role not in ['super_admin', 'admin']:
            return HttpResponse("Rôle invalide ❌")

        try:
            member = Member.objects.get(nim=nim)
        except Member.DoesNotExist:
            return HttpResponse("Aucun membre trouvé avec ce NIM ❌")

        if AdminUser.objects.filter(nim=nim).exists():
            return HttpResponse("Un administrateur existe déjà avec ce NIM ❌")

        if AdminUser.objects.filter(email=email).exists():
            return HttpResponse("Cet email existe déjà ❌")

        if role == 'super_admin' and request.session.get('admin_email') != 'admin@fondaction.com':
            return HttpResponse("Seul le super admin principal peut créer un super admin ❌")

        temporary_password = generate_temporary_password()

        new_admin = AdminUser.objects.create(
            first_name=member.first_name,
            last_name=member.last_name,
            phone=member.phone,
            nim=member.nim,
            email=email,
            password=make_password(temporary_password),
            role=role,
            status=ADMIN_STATUS_ACTIVE,
            must_change_password=True
        )

        current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

        log_activity(
            admin_user=current_admin,
            action='create_admin',
            target_type='admin',
            target_id=new_admin.id,
            details=f"{current_admin.email} a créé l’admin {new_admin.email} lié au NIM {new_admin.nim}"
        )

        return HttpResponse(
            f"Administrateur créé avec succès ✅<br>"
            f"Mot de passe provisoire : <strong>{temporary_password}</strong><br>"
            f"L’administrateur devra changer ce mot de passe à sa première connexion."
        )

    return render(request, 'admins/create_admin.html')


@admin_session_required
def admin_detail(request, admin_id):
    if request.session.get('admin_role') != 'super_admin':
        return HttpResponse("Accès refusé ❌")

    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    total_created_members = Member.objects.filter(created_by=admin).count()

    return render(request, 'admins/admin_detail.html', {
        'admin_obj': admin,
        'total_created_members': total_created_members,
    })


@super_admin_required
def reset_admin_password(request, admin_id):
    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    if admin.role == 'super_admin' and request.session.get('admin_email') != 'admin@fondaction.com':
        return HttpResponse("Seul le super admin principal peut réinitialiser le mot de passe d’un super admin ❌")

    temporary_password = generate_temporary_password()
    admin.password = make_password(temporary_password)
    admin.must_change_password = True
    admin.save(update_fields=['password', 'must_change_password', 'updated_at'])

    current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

    log_activity(
        admin_user=current_admin,
        action='reset_admin_password',
        target_type='admin',
        target_id=admin.id,
        details=f"{current_admin.email} a réinitialisé le mot de passe de {admin.email}"
    )

    return HttpResponse(
        f"Mot de passe réinitialisé avec succès ✅<br>"
        f"Nouveau mot de passe provisoire : <strong>{temporary_password}</strong><br>"
        f"L’administrateur devra le changer à sa prochaine connexion."
    )


@super_admin_required
def suspend_admin(request, admin_id):
    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    if admin.id == request.session.get('admin_id'):
        return HttpResponse("Tu ne peux pas te suspendre toi-même ❌")

    if admin.role == 'super_admin':
        return HttpResponse("Impossible de suspendre un super admin ❌")

    admin.status = ADMIN_STATUS_SUSPENDED
    admin.save(update_fields=['status', 'updated_at'])

    current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

    log_activity(
        admin_user=current_admin,
        action='suspend_admin',
        target_type='admin',
        target_id=admin.id,
        details=f"{current_admin.email} a suspendu {admin.email}"
    )

    return redirect('/admins/list/')


@super_admin_required
def reactivate_admin(request, admin_id):
    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    admin.status = ADMIN_STATUS_ACTIVE
    admin.save(update_fields=['status', 'updated_at'])

    current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

    log_activity(
        admin_user=current_admin,
        action='reactivate_admin',
        target_type='admin',
        target_id=admin.id,
        details=f"{current_admin.email} a réactivé {admin.email}"
    )

    return redirect('/admins/list/')


@super_admin_required
def activity_logs(request):
    from logs.models import ActivityLog

    logs = ActivityLog.objects.all().order_by('-created_at')
    return render(request, 'admins/activity_logs.html', {
        'logs': logs
    })


@admin_session_required
def create_member(request):
    if request.method == 'POST':
        try:
            current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))
        except AdminUser.DoesNotExist:
            request.session.flush()
            return redirect('/admins/login/')

        try:
            validate_uploaded_image(request.FILES.get('photo'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
            validate_uploaded_image(request.FILES.get('id_card_front'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
            validate_uploaded_image(request.FILES.get('id_card_back'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
            validate_uploaded_image(request.FILES.get('signature'), ['.png'], max_size_mb=2)

            member = create_member_record(request.POST, request.FILES, current_admin)
        except ValueError as e:
            return HttpResponse(f"{str(e)} ❌")
        except Exception:
            return HttpResponse("Erreur serveur ❌")

        log_activity(
            admin_user=current_admin,
            action='create_member',
            target_type='member',
            target_id=member.id,
            details=f"{current_admin.email} a créé le membre {member.nim}"
        )

        return redirect('/admins/members/')

    return render(request, 'admins/create_member.html')


@admin_session_required
def member_list(request):
    try:
        current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))
    except AdminUser.DoesNotExist:
        request.session.flush()
        return redirect('/admins/login/')

    nim = (request.GET.get('nim') or '').strip()
    phone = (request.GET.get('phone') or '').strip()

    members = Member.objects.filter(
        created_by=current_admin
    ).order_by('-created_at')

    if nim:
        members = members.filter(nim__icontains=nim)

    if phone:
        members = members.filter(phone__icontains=phone)

    return render(request, 'admins/member_list.html', {
        'members': members,
        'admin': current_admin,
        'nim': nim,
        'phone': phone,
    })

@admin_session_required
def member_detail(request, member_id):
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse("Membre introuvable ❌")

    forbidden = forbid_if_no_member_access(request, member)
    if forbidden:
        return forbidden

    transactions = MemberTransaction.objects.filter(
        member=member
    ).order_by('-created_at')

    return render(request, 'admins/member_detail.html', {
        'member': member,
        'transactions': transactions,
    })


def member_login(request):
    if request.method == 'POST':
        nim = (request.POST.get('nim') or '').strip()
        pin = (request.POST.get('pin') or '').strip()

        try:
            member = Member.objects.get(nim=nim)

            if member.status == MEMBER_STATUS_SUSPENDED:
                return HttpResponse("Compte suspendu ❌")

            if member.status != MEMBER_STATUS_ACTIVE:
                return HttpResponse("Compte membre inactif ❌")

            if member.is_locked:
                return HttpResponse("Compte bloqué ❌ Veuillez contacter l’administration pour une réinitialisation.")

            if check_password(pin, member.member_pin):
                member.failed_pin_attempts = 0
                member.save(update_fields=['failed_pin_attempts'])

                request.session['member_id'] = member.id
                request.session['member_nim'] = member.nim
                request.session['member_name'] = f"{member.first_name} {member.last_name}"

                if member.must_change_pin:
                    return redirect('/admins/member-change-pin/')

                return redirect('/admins/member-space/')

            member.failed_pin_attempts += 1

            if member.failed_pin_attempts >= MAX_MEMBER_PIN_ATTEMPTS:
                member.is_locked = True
                member.save(update_fields=['failed_pin_attempts', 'is_locked'])
                return HttpResponse(
                    "Compte bloqué ❌ Vous avez dépassé 3 tentatives incorrectes. "
                    "Veuillez contacter l’administration pour une réinitialisation."
                )

            member.save(update_fields=['failed_pin_attempts'])
            remaining = MAX_MEMBER_PIN_ATTEMPTS - member.failed_pin_attempts
            return HttpResponse(f"PIN incorrect ❌ Il vous reste {remaining} tentative(s).")

        except Member.DoesNotExist:
            return HttpResponse("Membre introuvable ❌")

    return render(request, 'admins/member_login.html')


@member_session_required
def member_change_pin(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    if request.method == 'POST':
        new_pin = request.POST.get('new_pin')
        confirm_pin = request.POST.get('confirm_pin')

        if not new_pin or not new_pin.isdigit() or len(new_pin) != 5:
            return HttpResponse("Le nouveau PIN doit contenir exactement 5 chiffres ❌")

        if new_pin != confirm_pin:
            return HttpResponse("Les deux PIN ne correspondent pas ❌")

        member.member_pin = make_password(new_pin)
        member.must_change_pin = False
        member.failed_pin_attempts = 0
        member.is_locked = False
        member.save(update_fields=['member_pin', 'must_change_pin', 'failed_pin_attempts', 'is_locked'])

        return redirect('/admins/member-space/')

    return render(request, 'admins/member_change_pin.html')


@admin_session_required  # ou member session selon ton système
def member_space(request):
    member_id = request.session.get('member_id')

    if not member_id:
        return redirect('/admins/member-login/')

    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    total_contributions = get_total_contributions(member)
    available_balance = get_available_balance(member)
    recent_transactions = get_recent_transactions(member)

    return render(request, 'admins/member_space.html', {
        'member': member,
        'total_contributions': total_contributions,
        'available_balance': available_balance,
        'recent_transactions': recent_transactions,
    })

@admin_session_required
def member_withdrawal(request):
    member_id = request.session.get('member_id')

    if not member_id:
        return redirect('/admins/member-login/')

    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    error_message = None
    success_message = None

    if request.method == 'POST':
        amount = (request.POST.get('amount') or '').strip()
        receiver_phone = (request.POST.get('receiver_phone') or '').strip()
        reason = (request.POST.get('reason') or '').strip()
        pin = (request.POST.get('pin') or '').strip()

        try:
            create_withdrawal_request(
                member=member,
                amount=amount,
                receiver_phone=receiver_phone,
                reason=reason,
                pin=pin,
            )
            success_message = "Votre demande de retrait a été envoyée avec succès. Elle est en attente de validation."
        except ValueError as e:
            error_message = str(e)
        except Exception:
            error_message = "Une erreur est survenue lors de la demande de retrait."

    available_balance = get_available_balance(member)

    return render(request, 'admins/member_withdrawal.html', {
        'member': member,
        'available_balance': available_balance,
        'error_message': error_message,
        'success_message': success_message,
    })

@admin_session_required
def withdrawal_requests(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('/admins/login/')

    requests_list = WithdrawalRequest.objects.select_related(
        'member',
        'transaction',
        'processed_by',
    ).order_by('-created_at')

    return render(request, 'admins/withdrawal_requests.html', {
        'requests_list': requests_list,
    })


@admin_session_required
def approve_withdrawal(request, withdrawal_id):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('/admins/login/')

    if request.method != 'POST':
        return redirect('/admins/withdrawal-requests/')

    try:
        admin_user = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        request.session.flush()
        return redirect('/admins/login/')

    withdrawal_request = get_object_or_404(WithdrawalRequest, id=withdrawal_id)

    admin_note = (request.POST.get('admin_note') or '').strip()

    try:
        approve_withdrawal_request(
            withdrawal_request=withdrawal_request,
            admin_user=admin_user,
            admin_note=admin_note,
        )
    except ValueError as e:
        return HttpResponse(str(e))
    except Exception:
        return HttpResponse("Erreur lors de la validation du retrait.")

    return redirect('/admins/withdrawal-requests/')


@admin_session_required
def reject_withdrawal(request, withdrawal_id):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('/admins/login/')

    if request.method != 'POST':
        return redirect('/admins/withdrawal-requests/')

    try:
        admin_user = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        request.session.flush()
        return redirect('/admins/login/')

    withdrawal_request = get_object_or_404(WithdrawalRequest, id=withdrawal_id)

    admin_note = (request.POST.get('admin_note') or '').strip()

    try:
        reject_withdrawal_request(
            withdrawal_request=withdrawal_request,
            admin_user=admin_user,
            admin_note=admin_note,
        )
    except ValueError as e:
        return HttpResponse(str(e))
    except Exception:
        return HttpResponse("Erreur lors du refus du retrait.")

    return redirect('/admins/withdrawal-requests/')





@member_session_required
def member_logout(request):
    request.session.pop('member_id', None)
    request.session.pop('member_nim', None)
    request.session.pop('member_name', None)
    return redirect('/admins/member-login/')


@super_admin_required
def reset_member_pin(request, member_id):
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse("Membre introuvable ❌")

    temporary_pin = generate_temporary_pin()
    member.member_pin = make_password(temporary_pin)
    member.must_change_pin = True
    member.failed_pin_attempts = 0
    member.is_locked = False
    member.save(update_fields=['member_pin', 'must_change_pin', 'failed_pin_attempts', 'is_locked'])

    current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

    log_activity(
        admin_user=current_admin,
        action='reset_member_pin',
        target_type='member',
        target_id=member.id,
        details=f"{current_admin.email} a réinitialisé le PIN du membre {member.nim}"
    )

    return HttpResponse(
        f"PIN réinitialisé avec succès ✅<br>"
        f"Nouveau PIN provisoire : <strong>{temporary_pin}</strong><br>"
        f"Le membre devra le changer à la prochaine connexion."
    )


@member_session_required
def member_card(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    return render(request, 'admins/member_card.html', {
        'member': member
    })


@member_session_required
def download_member_card_pdf(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    template = get_template('admins/member_card_pdf.html')
    html = template.render({
        'member': member,
        'photo_url': request.build_absolute_uri(member.photo.url) if member.photo else '',
        'signature_url': request.build_absolute_uri(member.signature.url) if member.signature else '',
        'logo_url': request.build_absolute_uri('/static/logo-fondaction.png'),
        'card_bg_url': request.build_absolute_uri('/static/card-bg.png'),
        'card_back_bg_url': request.build_absolute_uri('/static/card-back-bg.png'),
    })

    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

    if pdf.err:
        return HttpResponse("Erreur lors de la génération du PDF ❌")

    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="carte_{member.nim}.pdf"'
    return response

@admin_session_required
def edit_member(request, member_id):
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse("Membre introuvable ❌")

    forbidden = forbid_if_no_member_access(request, member)
    if forbidden:
        return forbidden

    if request.method == 'POST':
        member.first_name = (request.POST.get('first_name') or '').strip()
        member.last_name = (request.POST.get('last_name') or '').strip()
        member.birth_date = request.POST.get('birth_date')
        member.birth_place = (request.POST.get('birth_place') or '').strip()
        member.department = (request.POST.get('department') or '').strip()
        member.commune = (request.POST.get('commune') or '').strip()
        member.city = (request.POST.get('city') or '').strip()
        member.district = (request.POST.get('district') or '').strip()
        member.phone = (request.POST.get('phone') or '').strip() or None
        member.id_card_type = (request.POST.get('id_card_type') or '').strip()
        member.id_card_number = (request.POST.get('id_card_number') or '').strip()
        member.emergency_last_name = (request.POST.get('emergency_last_name') or '').strip() or None
        member.emergency_first_name = (request.POST.get('emergency_first_name') or '').strip() or None
        member.emergency_phone = (request.POST.get('emergency_phone') or '').strip() or None

        if not member.id_card_number:
            return HttpResponse("Le numéro de pièce est obligatoire ❌")

        if Member.objects.filter(id_card_number=member.id_card_number).exclude(id=member.id).exists():
            return HttpResponse("Un autre membre utilise déjà ce numéro de pièce ❌")

        if member.phone and Member.objects.filter(phone=member.phone).exclude(id=member.id).exists():
            return HttpResponse("Un autre membre utilise déjà ce numéro de téléphone ❌")

        try:
            validate_uploaded_image(request.FILES.get('photo'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
            validate_uploaded_image(request.FILES.get('id_card_front'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
            validate_uploaded_image(request.FILES.get('id_card_back'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
            validate_uploaded_image(request.FILES.get('signature'), ['.png'], max_size_mb=2)
        except ValueError as e:
            return HttpResponse(f"{str(e)} ❌")

        if request.FILES.get('photo'):
            member.photo = request.FILES.get('photo')

        if request.FILES.get('id_card_front'):
            member.id_card_front = request.FILES.get('id_card_front')

        if request.FILES.get('id_card_back'):
            member.id_card_back = request.FILES.get('id_card_back')

        if request.FILES.get('signature'):
            member.signature = request.FILES.get('signature')

        member.save()

        try:
            current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))
        except AdminUser.DoesNotExist:
            request.session.flush()
            return redirect('/admins/login/')

        log_activity(
            admin_user=current_admin,
            action='edit_member',
            target_type='member',
            target_id=member.id,
            details=f"{current_admin.email} a modifié le membre {member.nim}"
        )

        return redirect(f'/admins/members/{member.id}/')

    return render(request, 'admins/edit_member.html', {
        'member': member
    })


@admin_session_required
def suspend_member(request, member_id):
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse("Membre introuvable ❌")

    forbidden = forbid_if_no_member_access(request, member)
    if forbidden:
        return forbidden

    member.status = MEMBER_STATUS_SUSPENDED
    member.save(update_fields=['status'])

    current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

    log_activity(
        admin_user=current_admin,
        action='suspend_member',
        target_type='member',
        target_id=member.id,
        details=f"{current_admin.email} a suspendu le membre {member.nim}"
    )

    return redirect(f'/admins/members/{member.id}/')


@admin_session_required
def activate_member(request, member_id):
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse("Membre introuvable ❌")

    forbidden = forbid_if_no_member_access(request, member)
    if forbidden:
        return forbidden

    member.status = MEMBER_STATUS_ACTIVE
    member.save(update_fields=['status'])

    current_admin = AdminUser.objects.get(id=request.session.get('admin_id'))

    log_activity(
        admin_user=current_admin,
        action='activate_member',
        target_type='member',
        target_id=member.id,
        details=f"{current_admin.email} a réactivé le membre {member.nim}"
    )

    return redirect(f'/admins/members/{member.id}/')


@admin_session_required
def member_creation_history(request):
    admin_id = request.session.get('admin_id')
    role = request.session.get('admin_role')

    if role == 'super_admin':
        members = Member.objects.all().order_by('-created_at')
    else:
        members = Member.objects.filter(created_by_id=admin_id).order_by('-created_at')

    return render(request, 'admins/member_creation_history.html', {
        'members': members,
        'role': role,
    })


@super_admin_required
def admin_performance_detail(request, admin_id):
    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    members = Member.objects.filter(created_by=admin).order_by('-created_at')

    if start_date:
        members = members.filter(created_at__date__gte=start_date)

    if end_date:
        members = members.filter(created_at__date__lte=end_date)

    total_members = members.count()

    return render(request, 'admins/admin_performance_detail.html', {
        'admin_obj': admin,
        'members': members,
        'total_members': total_members,
        'start_date': start_date,
        'end_date': end_date,
    })


@super_admin_required
def export_admin_performance_excel(request, admin_id):
    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    members = Member.objects.filter(created_by=admin).order_by('-created_at')

    if start_date:
        members = members.filter(created_at__date__gte=start_date)

    if end_date:
        members = members.filter(created_at__date__lte=end_date)

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Performance Admin"

    headers = [
        "Admin NIM",
        "Admin Nom",
        "Admin Prénom",
        "Admin Email",
        "Rôle",
        "Membre NIM",
        "Membre Nom",
        "Membre Prénom",
        "Téléphone membre",
        "Date de création"
    ]
    sheet.append(headers)

    for member in members:
        sheet.append([
            admin.nim,
            admin.last_name,
            admin.first_name,
            admin.email,
            admin.role,
            member.nim,
            member.last_name,
            member.first_name,
            member.phone,
            member.created_at.strftime("%d/%m/%Y %H:%M")
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename=performance_{admin.id}.xlsx'

    workbook.save(response)
    return response


@admin_session_required
def export_members_excel(request):
    role = request.session.get('admin_role')
    admin_id = request.session.get('admin_id')

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Membres"

    headers = [
        "NIM",
        "Nom",
        "Prénom",
        "Téléphone",
        "Ville",
        "Date de création",
        "Créé par"
    ]
    sheet.append(headers)

    members = Member.objects.all().order_by('-created_at')
    if role != 'super_admin':
        members = members.filter(created_by_id=admin_id)

    for member in members:
        sheet.append([
            member.nim,
            member.last_name,
            member.first_name,
            member.phone,
            member.city,
            member.created_at.strftime("%d/%m/%Y %H:%M"),
            member.created_by.email if member.created_by else ""
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=liste_membres.xlsx'

    workbook.save(response)
    return response


@super_admin_required
def export_admins_excel(request):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Admins"

    headers = [
        "ID",
        "Nom",
        "Prénom",
        "Email",
        "Téléphone",
        "Rôle",
        "Statut",
        "Date de création"
    ]
    sheet.append(headers)

    admins = AdminUser.objects.all().order_by('-created_at')

    for admin in admins:
        sheet.append([
            admin.id,
            admin.last_name,
            admin.first_name,
            admin.email,
            admin.phone,
            admin.role,
            admin.status,
            admin.created_at.strftime("%d/%m/%Y %H:%M") if admin.created_at else ""
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=liste_admins.xlsx'

    workbook.save(response)
    return response


@member_session_required
def member_payment(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    now = timezone.localtime()
    french_months = {
        1: "Janvier",
        2: "Février",
        3: "Mars",
        4: "Avril",
        5: "Mai",
        6: "Juin",
        7: "Juillet",
        8: "Août",
        9: "Septembre",
        10: "Octobre",
        11: "Novembre",
        12: "Décembre",
    }

    current_month_label = f"{french_months[now.month]} {now.year}"

    return render(request, 'admins/payment_page.html', {
        'member': member,
        'current_month_label': current_month_label,
        'amount': DEFAULT_MONTHLY_CONTRIBUTION,
    })


@member_session_required
def start_member_payment_view(request):
    if request.method != 'POST':
        return redirect('/admins/member-payment/')

    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    try:
        payment_url, _attempt = start_fedapay_payment(
            member=member,
            amount=DEFAULT_MONTHLY_CONTRIBUTION,
            months=DEFAULT_PAYMENT_MONTHS,
            callback_url=request.build_absolute_uri('/admins/payment-return/'),
        )
        return redirect(payment_url)
    except Exception as e:
        return HttpResponse(f"Erreur paiement : {str(e)} ❌")


def start_member_payment(request):
    return start_member_payment_view(request)


@member_session_required
def payment_return(request):
    status = request.GET.get('status', '')
    transaction_id = request.GET.get('id', '')

    return render(request, 'admins/payment_return.html', {
        'status': status,
        'transaction_id': transaction_id,
    })


@member_session_required
def member_transactions(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    transactions = MemberTransaction.objects.filter(
        member=member
    ).order_by('-created_at')

    return render(request, 'admins/member_transactions.html', {
        'member': member,
        'transactions': transactions
    }) 

@member_session_required
def member_transaction_detail(request, transaction_id):
    member_id = request.session.get('member_id')

    if not member_id:
        return redirect('/admins/member-login/')

    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    transaction = get_object_or_404(
        MemberTransaction,
        id=transaction_id,
        member=member
    )

    withdrawal_request = None
    try:
        withdrawal_request = transaction.withdrawal_request
    except WithdrawalRequest.DoesNotExist:
        withdrawal_request = None
    except AttributeError:
        withdrawal_request = None

    return render(request, 'admins/member_transaction_detail.html', {
        'member': member,
        'transaction': transaction,
        'withdrawal_request': withdrawal_request,
    })   

@member_session_required
def member_profile(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    return render(request, 'admins/member_profile.html', {
        'member': member
    })

@member_session_required
def member_settings(request):
    try:
        member = Member.objects.get(id=request.session.get('member_id'))
    except Member.DoesNotExist:
        request.session.flush()
        return redirect('/admins/member-login/')

    return render(request, 'admins/member_settings.html', {
        'member': member
    })


@admin_session_required
def search_transactions(request):
    admin_id = request.session.get('admin_id')

    if not admin_id:
        return redirect('/admins/login/')

    query = (request.GET.get('q') or '').strip()
    transactions = []

    if query:
        transactions = MemberTransaction.objects.select_related('member').filter(
            receipt_number__icontains=query
        ).order_by('-created_at')

    return render(request, 'admins/search_transactions.html', {
        'query': query,
        'transactions': transactions,
    })

def member_assistance(request):
    return render(request, 'admins/member_assistance.html')




import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("DJANGO_SECRET_KEY manquant dans le .env")

DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

DATABASE_ENGINE = os.getenv("DATABASE_ENGINE", "sqlite")
if not DEBUG and DATABASE_ENGINE == "sqlite":
    print("ATTENTION: le projet tourne en production avec SQLite")

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
    if host.strip()
]

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'admins',
    'members',
    'logs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

if DATABASE_ENGINE == "postgres":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB', ''),
            'USER': os.getenv('POSTGRES_USER', ''),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
            'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
            'PORT': os.getenv('POSTGRES_PORT', '5432'),
            'CONN_MAX_AGE': 60,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Porto-Novo'
USE_I18N = True
USE_TZ = True

CORS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("DJANGO_CORS_ALLOWED_ORIGINS", "").split(",")
    if origin.strip()
]
CORS_ALLOW_CREDENTIALS = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

FEDAPAY_MODE = os.getenv("FEDAPAY_MODE", "sandbox")
FEDAPAY_PUBLIC_KEY = os.getenv("FEDAPAY_PUBLIC_KEY", "")
FEDAPAY_SECRET_KEY = os.getenv("FEDAPAY_SECRET_KEY", "")

if FEDAPAY_MODE == "sandbox":
    FEDAPAY_API_BASE = "https://sandbox-api.fedapay.com/v1"
else:
    FEDAPAY_API_BASE = "https://api.fedapay.com/v1"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Sécurité production
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = False
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = os.getenv("DJANGO_SECURE_SSL_REDIRECT", "True") == "True"
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# Sessions
SESSION_COOKIE_AGE = 60 * 60 * 12  # 12 heures
SESSION_SAVE_EVERY_REQUEST = True




from django.db import models
from admins.models import AdminUser


class ActivityLog(models.Model):
    admin_user = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    target_type = models.CharField(max_length=50, null=True, blank=True)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, default='success')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admin_user.email} - {self.action}"





from decimal import Decimal

DEFAULT_MONTHLY_CONTRIBUTION = Decimal("1200.00")
DEFAULT_PAYMENT_MONTHS = 1

MEMBER_STATUS_ACTIVE = "active"
MEMBER_STATUS_SUSPENDED = "suspended"
MEMBER_STATUS_INACTIVE = "inactive"

ADMIN_STATUS_ACTIVE = "active"
ADMIN_STATUS_SUSPENDED = "suspended"
ADMIN_STATUS_INACTIVE = "inactive"

ADMIN_ROLE_SUPER = "super_admin"
ADMIN_ROLE_STANDARD = "admin"

MAX_MEMBER_PIN_ATTEMPTS = 3
TEMP_ADMIN_PASSWORD_LENGTH = 12
TEMP_MEMBER_PIN_LENGTH = 5



from django.db import models
from admins.models import AdminUser


class Member(models.Model):
    CARD_TYPE_CHOICES = [
        ('CIP', 'CIP'),
        ('NPI', 'NPI'),
        ('CEDEAO', 'CEDEAO'),
        ('PASSEPORT', 'PASSEPORT'),
    ]

    STATUS_CHOICES = [
        ('active', 'Actif'),
        ('inactive', 'Inactif'),
        ('suspended', 'Suspendu'),
    ]

    nim = models.CharField(max_length=20, unique=True, null=True, blank=True, db_index=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=150)
    department = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True, db_index=True)

    photo = models.ImageField(upload_to='members/photos/', null=True, blank=True)

    id_card_type = models.CharField(max_length=20, choices=CARD_TYPE_CHOICES)
    id_card_number = models.CharField(max_length=100, unique=True, db_index=True)
    id_card_front = models.ImageField(upload_to='members/id_cards/front/', null=True, blank=True)
    id_card_back = models.ImageField(upload_to='members/id_cards/back/', null=True, blank=True)

    signature = models.ImageField(upload_to='members/signatures/', null=True, blank=True)
    member_pin = models.CharField(max_length=255, null=True, blank=True)

    emergency_last_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_first_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_phone = models.CharField(max_length=20, null=True, blank=True)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    must_change_pin = models.BooleanField(default=False)
    failed_pin_attempts = models.PositiveIntegerField(default=0)
    is_locked = models.BooleanField(default=False)

    created_by = models.ForeignKey(AdminUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nim} - {self.first_name} {self.last_name}"


class MemberTransaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('payment', 'Paiement'),
        ('withdrawal', 'Retrait'),
    ]

    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('success', 'Succès'),
        ('failed', 'Échoué'),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reference = models.CharField(max_length=100, unique=True)
    receipt_number = models.CharField(max_length=30, unique=True, null=True, blank=True, db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    validated_at = models.DateTimeField(blank=True, null=True)


    class Meta:
        indexes = [
            models.Index(fields=['member', 'transaction_type', 'status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.reference} - {self.member.nim} - {self.transaction_type}"


class WithdrawalRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('approved', 'Approuvé'),
        ('rejected', 'Rejeté'),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='withdrawal_requests'
    )
    transaction = models.OneToOneField(
        MemberTransaction,
        on_delete=models.CASCADE,
        related_name='withdrawal_request'
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    receiver_phone = models.CharField(max_length=20)
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_note = models.TextField(blank=True, null=True)
    processed_by = models.ForeignKey(
        AdminUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='processed_withdrawals'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['member', 'status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"Retrait {self.member.nim} - {self.amount} - {self.status}"


class InfoPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='members/info_posts/images/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        AdminUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='info_posts'
    )

    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title


class FedapayPaymentAttempt(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
        ('failed', 'Failed'),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='fedapay_attempts'
    )
    transaction_id = models.CharField(max_length=100, unique=True)
    transaction_reference = models.CharField(max_length=150, blank=True, null=True)
    nim = models.CharField(max_length=50)
    months = models.PositiveIntegerField(default=1)
    monthly_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_url = models.TextField(blank=True, null=True)
    fedapay_payload = models.JSONField(blank=True, null=True)
    is_processed = models.BooleanField(default=False)
    processed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['member', 'status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.nim} - {self.transaction_id} - {self.status}"




from decimal import Decimal

import requests
from django.conf import settings
from django.db import transaction
from django.utils import timezone

from members.models import FedapayPaymentAttempt, MemberTransaction
from members.services import create_manual_payment_transaction


def build_fedapay_headers():
    return {
        "Authorization": f"Bearer {settings.FEDAPAY_SECRET_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def build_fedapay_verify_headers():
    return {
        "Authorization": f"Bearer {settings.FEDAPAY_SECRET_KEY}",
        "Accept": "application/json",
    }


def start_fedapay_payment(member, amount, months, callback_url):
    amount = Decimal(str(amount))
    total_amount = amount * Decimal(str(months))

    payload = {
        "description": f"Cotisation mensuelle - {member.nim}",
        "amount": float(total_amount),
        "currency": {"iso": "XOF"},
        "callback_url": callback_url,
        "customer": {
            "firstname": member.first_name or "",
            "lastname": member.last_name or "",
            "email": f"{member.nim.lower()}@fondaction.local",
            "phone_number": {
                "number": member.phone or "00000000",
                "country": "bj",
            }
        }
    }

    create_response = requests.post(
        f"{settings.FEDAPAY_API_BASE}/transactions",
        headers=build_fedapay_headers(),
        json=payload,
        timeout=30,
    )
    create_data = create_response.json()

    if create_response.status_code not in [200, 201]:
        raise ValueError(f"Erreur FedaPay création : {create_data}")

    transaction_data = (
        create_data.get('v1/transaction')
        or create_data.get('transaction')
        or create_data
    )

    transaction_id = transaction_data.get('id')
    transaction_reference = transaction_data.get('reference')

    if not transaction_id:
        raise ValueError("Transaction FedaPay introuvable")

    attempt, _ = FedapayPaymentAttempt.objects.update_or_create(
        transaction_id=str(transaction_id),
        defaults={
            'member': member,
            'nim': member.nim,
            'months': months,
            'monthly_amount': amount,
            'total_amount': total_amount,
            'transaction_reference': transaction_reference,
            'status': 'pending',
            'fedapay_payload': create_data,
        }
    )

    token_response = requests.post(
        f"{settings.FEDAPAY_API_BASE}/transactions/{transaction_id}/token",
        headers=build_fedapay_headers(),
        json={"transaction_id": transaction_id},
        timeout=30,
    )
    token_data = token_response.json()

    if token_response.status_code not in [200, 201]:
        raise ValueError(f"Erreur FedaPay token : {token_data}")

    payment_url = (
        token_data.get('url')
        or token_data.get('token', {}).get('url')
        or token_data.get('v1/token', {}).get('url')
    )

    if not payment_url:
        raise ValueError("Lien de paiement introuvable")

    attempt.payment_url = payment_url
    attempt.save(update_fields=['payment_url', 'updated_at'])

    return payment_url, attempt


@transaction.atomic
def process_fedapay_webhook(payload):
    entity = payload.get('entity') or {}
    transaction_data = entity.get('data') or entity
    transaction_id = transaction_data.get('id')

    if not transaction_id:
        raise ValueError("Transaction introuvable")

    try:
        attempt = FedapayPaymentAttempt.objects.select_for_update().get(
            transaction_id=str(transaction_id)
        )
    except FedapayPaymentAttempt.DoesNotExist:
        raise ValueError("Tentative de paiement inexistante")

    try:
        verify_response = requests.get(
            f"{settings.FEDAPAY_API_BASE}/transactions/{transaction_id}",
            headers=build_fedapay_verify_headers(),
            timeout=30,
        )
    except requests.RequestException:
        raise ValueError("Erreur réseau lors de la vérification FedaPay")

    if verify_response.status_code not in [200, 201]:
        raise ValueError("Vérification FedaPay échouée")

    try:
        verify_data = verify_response.json()
    except Exception:
        raise ValueError("Réponse FedaPay invalide")

    transaction_verified = (
        verify_data.get('v1/transaction')
        or verify_data.get('transaction')
        or verify_data
    )

    verified_status = (transaction_verified.get('status') or '').lower()
    amount = Decimal(str(transaction_verified.get('amount', 0)))

    attempt.fedapay_payload = verify_data

    # 🔴 Paiement refusé
    if verified_status in ['declined', 'failed', 'canceled', 'cancelled']:
        attempt.status = 'declined'
        attempt.save(update_fields=['status', 'fedapay_payload', 'updated_at'])
        return 'declined'

    # 🟡 En attente
    if verified_status not in ['approved', 'successful', 'success']:
        attempt.status = 'pending'
        attempt.save(update_fields=['status', 'fedapay_payload', 'updated_at'])
        return 'pending'

    # 🔁 Anti double traitement
    if attempt.is_processed:
        return 'already_processed'

    # 🔒 Vérification montant
    if amount != attempt.total_amount:
        raise ValueError("Montant incohérent")

    # 🔒 Vérification membre
    if not attempt.member:
        raise ValueError("Membre invalide")

    existing = MemberTransaction.objects.filter(
        member=attempt.member,
        reference=str(transaction_id)
    ).first()

    if not existing:
        create_manual_payment_transaction(
            member=attempt.member,
            amount=amount,
            description=f'Paiement FedaPay ({attempt.months} mois)',
            reference=str(transaction_id),
            validated_at=timezone.now(),
        )

    attempt.status = 'approved'
    attempt.is_processed = True
    attempt.processed_at = timezone.now()
    attempt.save(
        update_fields=[
            'status',
            'is_processed',
            'processed_at',
            'fedapay_payload',
            'updated_at'
        ]
    )

    return 'approved'




from django.http import HttpResponse

from admins.models import AdminUser


def get_current_admin(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return None

    try:
        return AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return None


def admin_can_access_member(request, member):
    role = request.session.get('admin_role')
    admin_id = request.session.get('admin_id')

    if role == 'super_admin':
        return True

    return member.created_by_id == admin_id


def forbid_if_no_member_access(request, member):
    if not admin_can_access_member(request, member):
        return HttpResponse("Accès refusé à ce membre ❌")
    return None




from decimal import Decimal
import uuid

from PIL import Image
from django.contrib.auth.hashers import make_password, check_password
from django.db import transaction
from django.db.models import Sum
from django.utils import timezone

from .models import Member, MemberTransaction, WithdrawalRequest


def generate_reference(prefix='TRX'):
    return f"{prefix}-{uuid.uuid4().hex[:10].upper()}"


def get_total_payments(member):
    result = MemberTransaction.objects.filter(
        member=member,
        transaction_type='payment',
        status='success'
    ).aggregate(total=Sum('amount'))
    return result['total'] or Decimal('0.00')


def get_total_success_withdrawals(member):
    result = MemberTransaction.objects.filter(
        member=member,
        transaction_type='withdrawal',
        status='success'
    ).aggregate(total=Sum('amount'))
    return result['total'] or Decimal('0.00')


def get_total_pending_withdrawals(member):
    result = MemberTransaction.objects.filter(
        member=member,
        transaction_type='withdrawal',
        status='pending'
    ).aggregate(total=Sum('amount'))
    return result['total'] or Decimal('0.00')


def get_total_contributions(member):
    total_payments = get_total_payments(member)
    total_success_withdrawals = get_total_success_withdrawals(member)

    total = total_payments - total_success_withdrawals

    if total <= 0:
        return Decimal('0.00')

    return total


def get_available_balance(member):
    total_payments = get_total_payments(member)
    total_success_withdrawals = get_total_success_withdrawals(member)
    total_pending_withdrawals = get_total_pending_withdrawals(member)

    available = total_payments - total_success_withdrawals - total_pending_withdrawals

    if available <= 0:
        return Decimal('0.00')

    return available


def get_recent_transactions(member, limit=5):
    return MemberTransaction.objects.filter(
        member=member
    ).order_by('-created_at')[:limit]


@transaction.atomic
def create_manual_payment_transaction(
    member,
    amount,
    description=None,
    reference=None,
    validated_at=None,
):
    amount = Decimal(str(amount))

    if amount <= 0:
        raise ValueError("Le montant doit être supérieur à zéro.")

    months = [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ]

    now = timezone.now()
    current_month = f"{months[now.month - 1]} {now.year}"

    if not description:
        description = f"Paiement mensuel - {current_month}"

    if not reference:
        reference = generate_reference('PAY')

    if validated_at is None:
        validated_at = timezone.now()

    transaction_record, created = MemberTransaction.objects.get_or_create(
        reference=reference,
        defaults={
            'member': member,
            'transaction_type': 'payment',
            'amount': amount,
            'status': 'success',
            'description': description,
            'validated_at': validated_at,
        }
    )

    if not transaction_record.receipt_number:
        transaction_record.receipt_number = generate_receipt_number(transaction_record)
        transaction_record.save(update_fields=['receipt_number'])

    return transaction_record


def generate_receipt_number(transaction):
    return f"RCPT-FAS-{transaction.created_at.year}-{transaction.id:08d}"    


@transaction.atomic
def create_withdrawal_request(member, amount, receiver_phone, reason, pin):
    amount = Decimal(str(amount))

    if amount <= 0:
        raise ValueError("Le montant doit être supérieur à zéro.")

    if not receiver_phone:
        raise ValueError("Le numéro destinataire est obligatoire.")

    if not pin:
        raise ValueError("Le code PIN est obligatoire.")

    member = Member.objects.select_for_update().get(pk=member.pk)

    if not member.member_pin or not check_password(pin, member.member_pin):
        raise ValueError("Code PIN incorrect.")

    available_balance = get_available_balance(member)
    if amount > available_balance:
        raise ValueError("Solde insuffisant pour effectuer ce retrait.")

    transaction_record = MemberTransaction.objects.create(
        member=member,
        transaction_type='withdrawal',
        amount=amount,
        reference=generate_reference('WDR'),
        status='pending',
        description='Retrait',
    )

    transaction_record.receipt_number = generate_receipt_number(transaction_record)
    transaction_record.save(update_fields=['receipt_number'])

    withdrawal_request = WithdrawalRequest.objects.create(
        member=member,
        transaction=transaction_record,
        amount=amount,
        receiver_phone=receiver_phone,
        reason=reason or '',
        status='pending',
    )

    return withdrawal_request


@transaction.atomic
def approve_withdrawal_request(withdrawal_request, admin_user, admin_note=None):
    withdrawal_request = WithdrawalRequest.objects.select_for_update().get(pk=withdrawal_request.pk)

    if withdrawal_request.status != 'pending':
        raise ValueError("Cette demande a déjà été traitée.")

    withdrawal_request.status = 'approved'
    withdrawal_request.admin_note = admin_note
    withdrawal_request.processed_by = admin_user
    withdrawal_request.processed_at = timezone.now()
    withdrawal_request.save(update_fields=[
        'status',
        'admin_note',
        'processed_by',
        'processed_at',
    ])

    transaction_record = withdrawal_request.transaction
    transaction_record.status = 'success'
    transaction_record.validated_at = timezone.now()
    transaction_record.save(update_fields=['status', 'validated_at'])

    return withdrawal_request


@transaction.atomic
def reject_withdrawal_request(withdrawal_request, admin_user, admin_note=None):
    withdrawal_request = WithdrawalRequest.objects.select_for_update().get(pk=withdrawal_request.pk)

    if withdrawal_request.status != 'pending':
        raise ValueError("Cette demande a déjà été traitée.")

    withdrawal_request.status = 'rejected'
    withdrawal_request.admin_note = admin_note
    withdrawal_request.processed_by = admin_user
    withdrawal_request.processed_at = timezone.now()
    withdrawal_request.save(update_fields=[
        'status',
        'admin_note',
        'processed_by',
        'processed_at',
    ])

    transaction_record = withdrawal_request.transaction
    transaction_record.status = 'failed'
    transaction_record.validated_at = timezone.now()
    transaction_record.save(update_fields=['status', 'validated_at'])

    return withdrawal_request


def validate_uploaded_image(uploaded_file, allowed_extensions=None, max_size_mb=5):
    if not uploaded_file:
        return

    allowed_extensions = allowed_extensions or ['.jpg', '.jpeg', '.png']

    filename = uploaded_file.name.lower()
    if not any(filename.endswith(ext) for ext in allowed_extensions):
        raise ValueError("Format de fichier non autorisé")

    if uploaded_file.size > max_size_mb * 1024 * 1024:
        raise ValueError(f"Le fichier dépasse {max_size_mb} Mo")

    try:
        uploaded_file.seek(0)
        img = Image.open(uploaded_file)
        img.verify()
        uploaded_file.seek(0)
    except Exception:
        raise ValueError("Fichier image invalide ou corrompu")


def create_member_record(data, files, current_admin):
    raw_pin = (data.get('member_pin') or '').strip()

    if not raw_pin or not raw_pin.isdigit() or len(raw_pin) != 5:
        raise ValueError("Le code PIN doit contenir exactement 5 chiffres")

    id_card_number = (data.get('id_card_number') or '').strip()
    phone = (data.get('phone') or '').strip() or None

    validate_uploaded_image(files.get('photo'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
    validate_uploaded_image(files.get('id_card_front'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
    validate_uploaded_image(files.get('id_card_back'), ['.jpg', '.jpeg', '.png'], max_size_mb=5)
    validate_uploaded_image(files.get('signature'), ['.png'], max_size_mb=2)

    if not id_card_number:
        raise ValueError("Le numéro de pièce est obligatoire")

    if Member.objects.filter(id_card_number=id_card_number).exists():
        raise ValueError("Un membre avec ce numéro de pièce existe déjà")

    if phone and Member.objects.filter(phone=phone).exists():
        raise ValueError("Un membre avec ce numéro de téléphone existe déjà")

    member = Member.objects.create(
        first_name=(data.get('first_name') or '').strip(),
        last_name=(data.get('last_name') or '').strip(),
        birth_date=data.get('birth_date'),
        birth_place=(data.get('birth_place') or '').strip(),
        department=(data.get('department') or '').strip(),
        commune=(data.get('commune') or '').strip(),
        city=(data.get('city') or '').strip(),
        district=(data.get('district') or '').strip(),
        phone=phone,
        photo=files.get('photo'),
        id_card_type=(data.get('id_card_type') or '').strip(),
        id_card_number=id_card_number,
        id_card_front=files.get('id_card_front'),
        id_card_back=files.get('id_card_back'),
        signature=files.get('signature'),
        member_pin=make_password(raw_pin),
        emergency_last_name=(data.get('emergency_last_name') or '').strip() or None,
        emergency_first_name=(data.get('emergency_first_name') or '').strip() or None,
        emergency_phone=(data.get('emergency_phone') or '').strip() or None,
        created_by=current_admin,
        status='active',
    )

    member.nim = f"FAS-{member.id:010d}"
    member.save(update_fields=['nim'])

    return member



DJANGO_SECRET_KEY=change-this-local-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DJANGO_CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000
DJANGO_CORS_ALLOWED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000

DATABASE_ENGINE=sqlite

FEDAPAY_MODE=sandbox
FEDAPAY_PUBLIC_KEY=pk_sandbox_jaHjXxytHbr850sAlKYuabvu
FEDAPAY_SECRET_KEY=sk_sandbox_EhhaVMxGTzD1LuGjXCuRPwjM



.env
venv/
__pycache__/
*.pyc
db.sqlite3
media/
staticfiles/