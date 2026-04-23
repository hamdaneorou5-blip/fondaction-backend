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