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

    attempt = FedapayPaymentAttempt.objects.select_for_update().get(
        transaction_id=str(transaction_id)
    )

    verify_response = requests.get(
        f"{settings.FEDAPAY_API_BASE}/transactions/{transaction_id}",
        headers=build_fedapay_verify_headers(),
        timeout=30,
    )

    if verify_response.status_code not in [200, 201]:
        raise ValueError(f"Vérification FedaPay échouée : {verify_response.text}")

    verify_data = verify_response.json()

    transaction_verified = (
        verify_data.get('v1/transaction')
        or verify_data.get('transaction')
        or verify_data
    )

    verified_status = (transaction_verified.get('status') or '').lower()
    amount = Decimal(str(transaction_verified.get('amount', 0)))

    attempt.fedapay_payload = verify_data

    if verified_status in ['declined', 'failed', 'canceled', 'cancelled']:
        attempt.status = 'declined'
        attempt.save(update_fields=['status', 'fedapay_payload', 'updated_at'])
        return 'declined'

    if verified_status not in ['approved', 'successful', 'success']:
        attempt.status = 'pending'
        attempt.save(update_fields=['status', 'fedapay_payload', 'updated_at'])
        return 'pending'

    if attempt.is_processed:
        return 'already_processed'

    if amount != attempt.total_amount:
        raise ValueError(
            f"Montant incohérent. Attendu={attempt.total_amount}, reçu={amount}"
        )

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