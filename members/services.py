from decimal import Decimal
from datetime import datetime
import uuid

from django.contrib.auth.hashers import make_password
from django.db import models, transaction
from django.db.models import Sum, Count
from django.utils import timezone

from .models import (
    Member,
    MemberTransaction,
    WithdrawalRequest,
    OfficialContract,
    MemberContractSubmission,
)


def generate_reference(prefix='TRX'):
    return f"{prefix}-{uuid.uuid4().hex[:10].upper()}"


def get_total_payments(member):
    result = MemberTransaction.objects.filter(
        member=member,
        transaction_type='payment',
        status='success'
    ).aggregate(total=Sum('amount'))
    return result['total'] or Decimal('0.00')


def get_total_withdrawals(member):
    result = MemberTransaction.objects.filter(
        member=member,
        transaction_type='withdrawal',
        status='success'
    ).aggregate(total=Sum('amount'))
    return result['total'] or Decimal('0.00')


def get_pending_withdrawals_total(member):
    result = WithdrawalRequest.objects.filter(
        member=member,
        status='pending'
    ).aggregate(total=Sum('amount'))
    return result['total'] or Decimal('0.00')


def get_total_contributions(member):
    total_payments = get_total_payments(member)
    total_withdrawals = get_total_withdrawals(member)
    remaining = total_payments - total_withdrawals

    if remaining <= 0:
        return Decimal('0.00')

    return remaining


def get_available_balance(member):
    total_payments = get_total_payments(member)
    total_withdrawals = get_total_withdrawals(member)
    pending_withdrawals = get_pending_withdrawals_total(member)

    balance = total_payments - total_withdrawals - pending_withdrawals

    if balance <= 0:
        return Decimal('0.00')

    return balance


def get_recent_transactions(member, limit=5):
    return MemberTransaction.objects.filter(
        member=member
    ).order_by('-created_at')[:limit]


def can_withdraw(member, amount):
    amount = Decimal(str(amount))
    if amount <= 0:
        return False
    return get_available_balance(member) >= amount


@transaction.atomic
def create_manual_payment_transaction(
    member,
    amount,
    description='Cotisation membre',
    reference=None,
    validated_at=None,
):
    amount = Decimal(str(amount))

    if amount <= 0:
        raise ValueError("Le montant doit être supérieur à zéro.")

    if not reference:
        reference = generate_reference('PAY')

    if validated_at is None:
        validated_at = timezone.now()

    transaction, created = MemberTransaction.objects.get_or_create(
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

    return transaction


@transaction.atomic
def create_withdrawal_request(member, amount, receiver_account, account_holder_name):
    amount = Decimal(str(amount))

    if amount <= 0:
        raise ValueError("Le montant doit être supérieur à zéro.")

    member = Member.objects.select_for_update().get(pk=member.pk)

    if not can_withdraw(member, amount):
        raise ValueError("Solde insuffisant pour effectuer ce retrait.")

    withdrawal = WithdrawalRequest.objects.create(
        member=member,
        amount=amount,
        receiver_account=receiver_account,
        account_holder_name=account_holder_name,
        status='pending'
    )

    return withdrawal


@transaction.atomic
def approve_withdrawal(withdrawal_request, admin=None, admin_note=None):
    withdrawal_request = WithdrawalRequest.objects.select_for_update().get(pk=withdrawal_request.pk)

    if withdrawal_request.status != 'pending':
        raise ValueError("Cette demande a déjà été traitée.")

    member = Member.objects.select_for_update().get(pk=withdrawal_request.member_id)

    total_payments = get_total_payments(member)
    total_withdrawals = get_total_withdrawals(member)

    other_pending = WithdrawalRequest.objects.filter(
        member=member,
        status='pending'
    ).exclude(pk=withdrawal_request.pk).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')

    available = total_payments - total_withdrawals - other_pending

    if available < withdrawal_request.amount:
        raise ValueError("Le solde du membre n'est plus suffisant.")

    withdrawal_request.status = 'approved'
    withdrawal_request.admin_note = admin_note
    withdrawal_request.processed_at = timezone.now()
    withdrawal_request.processed_by = admin
    withdrawal_request.save()

    transaction = MemberTransaction.objects.create(
        member=member,
        transaction_type='withdrawal',
        amount=withdrawal_request.amount,
        reference=generate_reference('WDR'),
        status='success',
        description='Retrait validé',
        validated_at=timezone.now(),
    )

    return transaction


@transaction.atomic
def reject_withdrawal(withdrawal_request, admin=None, admin_note=None):
    withdrawal_request = WithdrawalRequest.objects.select_for_update().get(pk=withdrawal_request.pk)

    if withdrawal_request.status != 'pending':
        raise ValueError("Cette demande a déjà été traitée.")

    withdrawal_request.status = 'rejected'
    withdrawal_request.admin_note = admin_note
    withdrawal_request.processed_at = timezone.now()
    withdrawal_request.processed_by = admin
    withdrawal_request.save()

    return withdrawal_request


def publish_info_post(post):
    post.is_published = True
    post.published_at = timezone.now()
    post.save()
    return post


def unpublish_info_post(post):
    post.is_published = False
    post.save()
    return post


def publish_project(project):
    project.is_published = True
    project.published_at = timezone.now()
    project.save()
    return project


def unpublish_project(project):
    project.is_published = False
    project.save()
    return project


def activate_contract(contract):
    OfficialContract.objects.filter(is_active=True).update(is_active=False)
    contract.is_active = True
    if not contract.published_at:
        contract.published_at = timezone.now()
    contract.save()
    return contract


def get_active_contract():
    return OfficialContract.objects.filter(is_active=True).order_by('-created_at').first()


def submit_member_contract(member, contract, signed_file):
    submission = MemberContractSubmission.objects.create(
        member=member,
        contract=contract,
        signed_file=signed_file,
        status='pending'
    )
    return submission


def approve_contract_submission(submission, admin_note=None):
    submission.status = 'approved'
    submission.admin_note = admin_note
    submission.reviewed_at = timezone.now()
    submission.save()
    return submission


def reject_contract_submission(submission, admin_note=None):
    submission.status = 'rejected'
    submission.admin_note = admin_note
    submission.reviewed_at = timezone.now()
    submission.save()
    return submission


def get_start_of_current_month():
    now = timezone.now()
    return datetime(now.year, now.month, 1, tzinfo=now.tzinfo)


def get_admin_paid_members_current_month(admin):
    start_month = get_start_of_current_month()

    paid_member_ids = MemberTransaction.objects.filter(
        member__created_by=admin,
        transaction_type='payment',
        status='success',
        created_at__gte=start_month
    ).values_list('member_id', flat=True).distinct()

    return Member.objects.filter(id__in=paid_member_ids).order_by('last_name', 'first_name')


def get_admin_unpaid_members_current_month(admin):
    start_month = get_start_of_current_month()

    paid_member_ids = MemberTransaction.objects.filter(
        member__created_by=admin,
        transaction_type='payment',
        status='success',
        created_at__gte=start_month
    ).values_list('member_id', flat=True).distinct()

    return Member.objects.filter(
        created_by=admin
    ).exclude(id__in=paid_member_ids).order_by('last_name', 'first_name')


def get_total_payments_today():
    today = timezone.now().date()

    result = MemberTransaction.objects.filter(
        transaction_type='payment',
        status='success',
        created_at__date=today
    ).aggregate(total=Sum('amount'))

    return result['total'] or Decimal('0.00')


def get_total_payments_current_month():
    now = timezone.now()

    result = MemberTransaction.objects.filter(
        transaction_type='payment',
        status='success',
        created_at__year=now.year,
        created_at__month=now.month
    ).aggregate(total=Sum('amount'))

    return result['total'] or Decimal('0.00')


def get_total_payments_current_year():
    now = timezone.now()

    result = MemberTransaction.objects.filter(
        transaction_type='payment',
        status='success',
        created_at__year=now.year
    ).aggregate(total=Sum('amount'))

    return result['total'] or Decimal('0.00')


def get_most_regular_members(limit=10):
    return (
        Member.objects.annotate(
            payments_count=Count(
                'transactions',
                filter=models.Q(
                    transactions__transaction_type='payment',
                    transactions__status='success'
                )
            )
        )
        .order_by('-payments_count', 'last_name', 'first_name')[:limit]
    )


def get_admin_total_paid_current_month(admin):
    start_month = get_start_of_current_month()

    result = MemberTransaction.objects.filter(
        member__created_by=admin,
        transaction_type='payment',
        status='success',
        created_at__gte=start_month
    ).aggregate(total=Sum('amount'))

    return result['total'] or Decimal('0.00')


def get_admin_paid_members_in_period(admin, start_date=None, end_date=None):
    transactions = MemberTransaction.objects.filter(
        member__created_by=admin,
        transaction_type='payment',
        status='success'
    )

    if start_date:
        transactions = transactions.filter(created_at__date__gte=start_date)

    if end_date:
        transactions = transactions.filter(created_at__date__lte=end_date)

    paid_member_ids = transactions.values_list('member_id', flat=True).distinct()

    return Member.objects.filter(id__in=paid_member_ids).order_by('last_name', 'first_name')


def get_admin_unpaid_members_in_period(admin, start_date=None, end_date=None):
    all_members = Member.objects.filter(created_by=admin)

    transactions = MemberTransaction.objects.filter(
        member__created_by=admin,
        transaction_type='payment',
        status='success'
    )

    if start_date:
        transactions = transactions.filter(created_at__date__gte=start_date)

    if end_date:
        transactions = transactions.filter(created_at__date__lte=end_date)

    paid_member_ids = transactions.values_list('member_id', flat=True).distinct()

    return all_members.exclude(id__in=paid_member_ids).order_by('last_name', 'first_name')


def get_admin_total_paid_in_period(admin, start_date=None, end_date=None):
    transactions = MemberTransaction.objects.filter(
        member__created_by=admin,
        transaction_type='payment',
        status='success'
    )

    if start_date:
        transactions = transactions.filter(created_at__date__gte=start_date)

    if end_date:
        transactions = transactions.filter(created_at__date__lte=end_date)

    result = transactions.aggregate(total=Sum('amount'))
    return result['total'] or Decimal('0.00')


def create_member_record(data, files, current_admin):
    raw_pin = (data.get('member_pin') or '').strip()

    if not raw_pin or not raw_pin.isdigit() or len(raw_pin) != 5:
        raise ValueError("Le code PIN doit contenir exactement 5 chiffres")

    id_card_number = (data.get('id_card_number') or '').strip()
    phone = (data.get('phone') or '').strip() or None

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