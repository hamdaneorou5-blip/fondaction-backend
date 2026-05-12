import openpyxl
from io import BytesIO
from datetime import timedelta
from django.http import JsonResponse
from django.core.cache import cache
from django.conf import settings

from django.db.models import Exists, OuterRef, Sum,  Q

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from django.template.loader import get_template
from django.utils import timezone
from xhtml2pdf import pisa
from members.models import InfoPost
from django.shortcuts import get_object_or_404
from admins.models import AdminUser
from decimal import Decimal
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


        if is_rate_limited(
            request,
            key_prefix='admin_login',
            max_attempts=settings.LOGIN_RATE_LIMIT_MAX_ATTEMPTS,
            window_seconds=settings.LOGIN_RATE_LIMIT_WINDOW_SECONDS
        ):
            return HttpResponse("Trop de tentatives. Veuillez réessayer dans 10 minutes.")

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
    search_nim = (request.GET.get('nim') or '').strip()

    admins = AdminUser.objects.all().order_by('-created_at')

    if search_nim:
        admins = admins.filter(nim__icontains=search_nim)

    return render(request, 'admins/admins_list.html', {
        'admins': admins,
        'search_nim': search_nim,
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


def get_admin_members_with_payment_status(admin, start_date='', end_date='', payment_status='all'):
    members = Member.objects.filter(created_by=admin).order_by('-created_at')

    if start_date:
        members = members.filter(created_at__date__gte=start_date)

    if end_date:
        members = members.filter(created_at__date__lte=end_date)

    paid_transactions = MemberTransaction.objects.filter(
        member=OuterRef('pk'),
        transaction_type='payment',
        status='success'
    )

    members = members.annotate(
        has_paid=Exists(paid_transactions)
    )

    if payment_status == 'paid':
        members = members.filter(has_paid=True)
    elif payment_status == 'unpaid':
        members = members.filter(has_paid=False)

    return members


def get_global_members_with_payment_status(start_date='', end_date='', payment_status='all'):
    members = Member.objects.select_related('created_by').order_by('-created_at')

    if start_date:
        members = members.filter(created_at__date__gte=start_date)

    if end_date:
        members = members.filter(created_at__date__lte=end_date)

    paid_transactions = MemberTransaction.objects.filter(
        member=OuterRef('pk'),
        transaction_type='payment',
        status='success'
    )

    members = members.annotate(
        has_paid=Exists(paid_transactions),
        total_paid_amount=Sum(
            'transactions__amount',
            filter=Q(
                transactions__transaction_type='payment',
                transactions__status='success'
            )
        )
    )

    if payment_status == 'paid':
        members = members.filter(has_paid=True)
    elif payment_status == 'unpaid':
        members = members.filter(has_paid=False)

    return members


@admin_session_required
def admin_detail(request, admin_id):
    if request.session.get('admin_role') != 'super_admin':
        return HttpResponse("Accès refusé ❌")

    try:
        admin = AdminUser.objects.get(id=admin_id)
    except AdminUser.DoesNotExist:
        return HttpResponse("Admin introuvable ❌")

    start_date = (request.GET.get('start_date') or '').strip()
    end_date = (request.GET.get('end_date') or '').strip()
    payment_status = (request.GET.get('payment_status') or 'all').strip()

    members = get_admin_members_with_payment_status(
        admin=admin,
        start_date=start_date,
        end_date=end_date,
        payment_status=payment_status,
    )

    total_created_members = get_admin_members_with_payment_status(
        admin=admin,
        start_date=start_date,
        end_date=end_date,
        payment_status='all',
    ).count()

    total_paid_members = get_admin_members_with_payment_status(
        admin=admin,
        start_date=start_date,
        end_date=end_date,
        payment_status='paid',
    ).count()

    total_unpaid_members = get_admin_members_with_payment_status(
        admin=admin,
        start_date=start_date,
        end_date=end_date,
        payment_status='unpaid',
    ).count()

    return render(request, 'admins/admin_detail.html', {
        'admin_obj': admin,
        'members': members,
        'total_created_members': total_created_members,
        'total_paid_members': total_paid_members,
        'total_unpaid_members': total_unpaid_members,
        'start_date': start_date,
        'end_date': end_date,
        'payment_status': payment_status,
    })


@super_admin_required
def global_admin_performance(request):
    start_date = (request.GET.get('start_date') or '').strip()
    end_date = (request.GET.get('end_date') or '').strip()
    payment_status = (request.GET.get('payment_status') or 'all').strip()

    members = get_global_members_with_payment_status(
        start_date=start_date,
        end_date=end_date,
        payment_status=payment_status,
    )

    total_created_members = get_global_members_with_payment_status(
        start_date=start_date,
        end_date=end_date,
        payment_status='all',
    ).count()

    total_paid_members = get_global_members_with_payment_status(
        start_date=start_date,
        end_date=end_date,
        payment_status='paid',
    ).count()

    total_unpaid_members = get_global_members_with_payment_status(
        start_date=start_date,
        end_date=end_date,
        payment_status='unpaid',
    ).count()

    total_admins = AdminUser.objects.count()
    total_members_all_time = Member.objects.count()

    payment_transactions = MemberTransaction.objects.filter(
        member__in=get_global_members_with_payment_status(
            start_date=start_date,
            end_date=end_date,
            payment_status='all',
        ),
        transaction_type='payment',
        status='success'
    )

    if start_date:
        payment_transactions = payment_transactions.filter(created_at__date__gte=start_date)

    if end_date:
        payment_transactions = payment_transactions.filter(created_at__date__lte=end_date)

    total_payments_amount = payment_transactions.aggregate(total=Sum('amount'))['total'] or 0

    admins_summary_data = []
    admins = AdminUser.objects.all().order_by('-created_at')

    for admin in admins:
        admin_members_in_period = Member.objects.filter(created_by=admin)

        if start_date:
            admin_members_in_period = admin_members_in_period.filter(created_at__date__gte=start_date)

        if end_date:
            admin_members_in_period = admin_members_in_period.filter(created_at__date__lte=end_date)

        created_count = admin_members_in_period.count()

        all_admin_members = Member.objects.filter(created_by=admin)

        paid_members = all_admin_members.filter(
            transactions__transaction_type='payment',
            transactions__status='success'
        )

        if start_date:
            paid_members = paid_members.filter(transactions__created_at__date__gte=start_date)

        if end_date:
            paid_members = paid_members.filter(transactions__created_at__date__lte=end_date)

        paid_count = paid_members.distinct().count()

        unpaid_count = created_count - paid_count
        salary_total = paid_count * 100

        admins_summary_data.append({
            'admin': admin,
            'created_count': created_count,
            'paid_count': paid_count,
            'unpaid_count': unpaid_count,
            'salary_total': salary_total,
        })

    admins_summary_data.sort(key=lambda x: x['created_count'], reverse=True)

    return render(request, 'admins/global_admin_performance.html', {
        'members': members,
        'total_created_members': total_created_members,
        'total_paid_members': total_paid_members,
        'total_unpaid_members': total_unpaid_members,
        'total_admins': total_admins,
        'total_members_all_time': total_members_all_time,
        'total_payments_amount': total_payments_amount,
        'admins_summary_data': admins_summary_data,
        'start_date': start_date,
        'end_date': end_date,
        'payment_status': payment_status,
    })


@super_admin_required
def export_global_admin_performance_excel(request):
    start_date = (request.GET.get('start_date') or '').strip()
    end_date = (request.GET.get('end_date') or '').strip()
    payment_status = (request.GET.get('payment_status') or 'all').strip()

    members = get_global_members_with_payment_status(
        start_date=start_date,
        end_date=end_date,
        payment_status=payment_status,
    )

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Performance Globale"

    headers = [
        "Admin créateur",
        "Email admin",
        "Rôle admin",
        "Membre NIM",
        "Nom membre",
        "Prénom membre",
        "Téléphone membre",
        "Ville",
        "Date de création",
        "A payé ?",
        "Montant total payé",
    ]
    sheet.append(headers)

    for member in members:
        admin = member.created_by

        total_paid_amount = MemberTransaction.objects.filter(
            member=member,
            transaction_type='payment',
            status='success'
        ).aggregate(total=Sum('amount'))['total'] or 0

        sheet.append([
            f"{admin.last_name} {admin.first_name}" if admin else "",
            admin.email if admin else "",
            admin.role if admin else "",
            member.nim,
            member.last_name,
            member.first_name,
            member.phone,
            member.city,
            member.created_at.strftime("%d/%m/%Y %H:%M"),
            "Oui" if member.has_paid else "Non",
            float(total_paid_amount),
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = (
        f'attachment; filename=performance_globale_{payment_status}.xlsx'
    )

    workbook.save(response)
    return response


@super_admin_required
def export_admins_summary_excel(request):
    start_date = (request.GET.get('start_date') or '').strip()
    end_date = (request.GET.get('end_date') or '').strip()

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Résumé Admins"

    headers = [
        "NIM Admin",
        "Nom",
        "Prénom",
        "Email",
        "Rôle",
        "Membres créés",
        "Ont payé",
        "N’ont pas payé",
        "Salaire total",
    ]
    sheet.append(headers)

    admins = AdminUser.objects.all().order_by('-created_at')

    for admin in admins:
        admin_members_in_period = Member.objects.filter(created_by=admin)

        if start_date:
            admin_members_in_period = admin_members_in_period.filter(created_at__date__gte=start_date)

        if end_date:
            admin_members_in_period = admin_members_in_period.filter(created_at__date__lte=end_date)

        created_count = admin_members_in_period.count()

        all_admin_members = Member.objects.filter(created_by=admin)

        paid_members = all_admin_members.filter(
            transactions__transaction_type='payment',
            transactions__status='success'
        )

        if start_date:
            paid_members = paid_members.filter(transactions__created_at__date__gte=start_date)

        if end_date:
            paid_members = paid_members.filter(transactions__created_at__date__lte=end_date)

        paid_count = paid_members.distinct().count()

        unpaid_count = created_count - paid_count
        salary_total = paid_count * 100

        sheet.append([
            admin.nim,
            admin.last_name,
            admin.first_name,
            admin.email,
            admin.role,
            created_count,
            paid_count,
            unpaid_count,
            salary_total,
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=resume_admins.xlsx'

    workbook.save(response)
    return response


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

    members = Member.objects.all().order_by('-created_at')

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

    total_contributions = MemberTransaction.objects.filter(
        member=member,
        transaction_type='payment',
        status='success'
    ).aggregate(total=Sum('amount'))['total'] or Decimal('0')

    total_withdrawals = MemberTransaction.objects.filter(
        member=member,
        transaction_type='withdrawal',
        status='success'
    ).aggregate(total=Sum('amount'))['total'] or Decimal('0')

    available_balance = total_contributions - total_withdrawals

    return render(request, 'admins/member_detail.html', {
        'member': member,
        'transactions': transactions,
        'total_contributions': total_contributions,
        'total_withdrawals': total_withdrawals,
        'available_balance': available_balance,
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

@member_session_required
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

@member_session_required
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

    start_date = (request.GET.get('start_date') or '').strip()
    end_date = (request.GET.get('end_date') or '').strip()
    payment_status = (request.GET.get('payment_status') or 'all').strip()

    members = get_admin_members_with_payment_status(
        admin=admin,
        start_date=start_date,
        end_date=end_date,
        payment_status=payment_status,
    )

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
        "Ville",
        "Date de création",
        "A payé ?",
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
            member.city,
            member.created_at.strftime("%d/%m/%Y %H:%M"),
            "Oui" if member.has_paid else "Non",
        ])

    filename_suffix = payment_status
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = (
        f'attachment; filename=performance_admin_{admin.id}_{filename_suffix}.xlsx'
    )

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


def visitor_home(request):
    return render(request, 'admins/visitor_home.html')

def secure_registration_page(request):
    return render(request, 'admins/secure_registration.html')

def about_page(request):
    return render(request, 'admins/about.html')

def privacy_policy_page(request):
    return render(request, 'admins/privacy_policy.html')


def terms_services_page(request):
    return render(request, 'admins/terms_services.html')

def contact_page(request):
    return render(request, 'admins/contact.html')


def root_router(request):
    host = request.get_host().split(':')[0]

    if host == "admin.fondactionsarl.com":
        return redirect('/admins/login/')

    if host == "api.fondactionsarl.com":
        return JsonResponse({
            "success": True,
            "message": "FondAction API is running"
        })

    return redirect('/admins/visiteur/')

def robots_txt(request):
    host = request.get_host()

    if host.startswith("admin.") or host.startswith("api."):
        return HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")

    return HttpResponse("User-agent: *\nAllow: /", content_type="text/plain")



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()

    return request.META.get('REMOTE_ADDR', '')


def is_rate_limited(request, key_prefix, max_attempts=5, window_seconds=600):
    ip = get_client_ip(request)
    cache_key = f"{key_prefix}:{ip}"

    attempts = cache.get(cache_key, 0)

    if attempts >= max_attempts:
        return True

    cache.set(cache_key, attempts + 1, timeout=window_seconds)
    return False


def sitemap_xml(request):
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://fondactionsarl.com/</loc>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://fondactionsarl.com/admins/about/</loc>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://fondactionsarl.com/admins/contact/</loc>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://fondactionsarl.com/admins/privacy-policy/</loc>
        <priority>0.5</priority>
    </url>
    <url>
        <loc>https://fondactionsarl.com/admins/terms-services/</loc>
        <priority>0.5</priority>
    </url>
</urlset>
"""
    return HttpResponse(xml, content_type="application/xml")





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


def validate_uploaded_image(uploaded_file, allowed_extensions=None, max_size_mb=20):
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



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paiement membre</title>
    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #111827;
        }

        body {
            padding-top: 0;
            padding-bottom: 100px;
        }

        .page {
            max-width: 520px;
            margin: 0 auto;
            padding: 18px 16px 0;
        }

        .topbar {
            background: white;
            border-radius: 24px;
            padding: 22px 18px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
            margin-bottom: 16px;
        }

        
        .topbar h1 {
            margin: 0 0 10px 0;
            font-size: 28px;
            color: #111827;
        }

        .back-btn {
    display: inline-block;
    margin-top: 12px;

    background: #111827;
    color: white;
    text-decoration: none;

    padding: 10px 16px;
    border-radius: 10px;

    font-size: 14px;
    font-weight: 600;

    transition: 0.2s ease;
}

/* effet hover pro */
.back-btn:hover {
    background: #000;
    transform: translateY(-1px);
}

        .card {
            background: white;
            border-radius: 24px;
            padding: 20px 16px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
        }

        .card h2 {
            margin-top: 0;
            margin-bottom: 18px;
            color: #111827;
            font-size: 22px;
        }

        .member-box {
            margin-bottom: 18px;
            padding: 16px;
            background: #f8fafc;
            border-radius: 16px;
            color: #374151;
            line-height: 1.7;
            font-size: 15px;
            border: 1px solid #e5e7eb;
        }

        .alert-success {
            margin-bottom: 16px;
            padding: 14px 16px;
            border-radius: 14px;
            background: #dcfce7;
            color: #166534;
            font-weight: bold;
            font-size: 14px;
            line-height: 1.6;
        }

        .alert-error {
            margin-bottom: 16px;
            padding: 14px 16px;
            border-radius: 14px;
            background: #fee2e2;
            color: #991b1b;
            font-weight: bold;
            font-size: 14px;
            line-height: 1.6;
        }

        .table-wrap {
            width: 100%;
            overflow-x: auto;
            margin-bottom: 18px;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
        }

        th, td {
            padding: 14px 12px;
            border-bottom: 1px solid #e5e7eb;
            text-align: left;
            font-size: 14px;
            vertical-align: top;
        }

        th {
            background: #f3f4f6;
            color: #111827;
            font-size: 13px;
        }

        tr:last-child td {
            border-bottom: none;
        }

        .amount {
            font-weight: bold;
            color: #166534;
            font-size: 16px;
        }

        .btn-submit {
            display: inline-block;
            width: 100%;
            border: none;
            background: #16a34a;
            color: white;
            padding: 14px 18px;
            border-radius: 14px;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
        }

        .btn-submit:hover {
            opacity: 0.92;
        }

        .info-note {
            margin-top: 16px;
            padding: 14px 16px;
            border-radius: 14px;
            background: #eff6ff;
            color: #1e3a8a;
            line-height: 1.7;
            font-size: 14px;
        }

        .resume-box {
            margin-top: 14px;
            padding: 14px 16px;
            border-radius: 14px;
            background: #f9fafb;
            color: #374151;
            line-height: 1.7;
            font-size: 14px;
            border: 1px solid #e5e7eb;
        }

        @media (max-width: 520px) {
            .topbar h1 {
                font-size: 24px;
            }

            .card h2 {
                font-size: 20px;
            }

            th, td {
                font-size: 13px;
                padding: 12px 10px;
            }

            .amount {
                font-size: 15px;
            }
        }
    </style>
</head>
<body>

    <div class="page">

    <div class="topbar">
    <h1>Paiement membre</h1>

    <a href="/admins/member-space/" class="back-btn">
         Retour à l’espace membre
    </a>
</div>

        <div class="card">
            <h2>Effectuer mon paiement</h2>

            {% if message %}
                <div class="alert-success">{{ message }}</div>
            {% endif %}

            {% if error %}
                <div class="alert-error">{{ error }}</div>
            {% endif %}

            <div class="member-box">
                <div><strong>Membre :</strong> {{ member.first_name }} {{ member.last_name }}</div>
                <div><strong>NIM :</strong> {{ member.nim }}</div>
                <div><strong>Téléphone :</strong> {{ member.phone }}</div>
            </div>

            <form method="POST" action="/admins/member-payment/start/">
                {% csrf_token %}

                <div class="table-wrap">
                    <table>
                        <tr>
                            <th>Libellé</th>
                            <th>Période</th>
                            <th>Montant</th>
                        </tr>
                        <tr>
                            <td>Paiement de cotisation mensuelle</td>
                            <td>{{ current_month_label }}</td>
                            <td class="amount">{{ amount }} FCFA</td>
                        </tr>
                    </table>
                </div>

                <button type="submit" class="btn-submit">Effectuer le paiement</button>
            </form>

            <div class="info-note">
                Le paiement affiché correspond automatiquement au mois en cours. Le montant mensuel est fixe et s'élève à <strong>1200,00 FCFA</strong>.
            </div>

            <div class="resume-box">
                Après validation, vous serez redirigé vers la plateforme de paiement sécurisée afin de finaliser votre cotisation mensuelle.
            </div>
        </div>
    </div>

</body>
</html>



<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Espace membre</title>
    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #111827;
        }

        body {
            padding-top: 78px;
            padding-bottom: 100px;
        }

        a {
            text-decoration: none;
        }

        .header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            height: 78px;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid #e5e7eb;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 18px;
        }

        .header-logo {
    display: flex;
    align-items: center;

    /* 👉 contrôle position horizontale */
    margin-left: 0px;   /* déplace à droite */
    margin-right: 0px;  /* déplace à gauche */
}

.header-logo img {
    /* 👉 contrôle taille */
    height: 85px;   /* change ici */
    width: auto;

    object-fit: contain;

    /* 👉 contrôle position fine */
    transform: translateX(-18px); /* décalage gauche/droite */
}

        .header-nim {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    background: #f1f5f9;
    padding: 8px 12px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    line-height: 1.2;
}

.nim-label {
    font-size: 10px;
    color: #6b7280;
    font-weight: 600;
    letter-spacing: 1px;
}

.nim-value {
    font-size: 13px;
    font-weight: bold;
    color: #111827;
}

        .page {
            max-width: 500px;
            margin: 0 auto;
            padding: 18px 16px 0;
        }

        .welcome-box {
            margin-top: 6px;
            margin-bottom: 18px;
        }

        .welcome-label {
            font-size: 15px;
            color: #6b7280;
            margin-bottom: 6px;
        }

        .welcome-name {
            font-size: 15px;
            color: #6b7280;
            margin-bottom: 4px;
        }

        .welcome-fullname {
            font-size: 28px;
            font-weight: bold;
            color: #111827;
            line-height: 1.25;
            word-break: break-word;
        }

        .balance-card {
            background: linear-gradient(135deg, #0f172a, #1e293b);
            border-radius: 28px;
            padding: 24px 20px;
            color: white;
            box-shadow: 0 16px 32px rgba(15, 23, 42, 0.18);
            margin-bottom: 24px;
        }

        .balance-label {
            font-size: 14px;
            color: rgba(255,255,255,0.78);
            margin-bottom: 10px;
        }

        .balance-value {
            font-size: 34px;
            font-weight: bold;
            line-height: 1.15;
            word-break: break-word;
            margin-bottom: 16px;
        }

        .balance-bottom {
            border-top: 1px solid rgba(255,255,255,0.12);
            padding-top: 14px;
        }

        .balance-text {
            margin: 0;
            font-size: 14px;
            color: rgba(255,255,255,0.88);
            line-height: 1.8;
        }

        .actions-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
        }

        .action-item {
            background: white;
            border-radius: 24px;
            padding: 18px 10px 16px;
            text-align: center;
            box-shadow: 0 12px 28px rgba(15, 23, 42, 0.07);
            border: 1px solid #edf2f7;
            min-height: 126px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 14px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .action-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 16px 30px rgba(15, 23, 42, 0.1);
        }

        .action-icon {
            width: 62px;
            height: 62px;
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #f8fafc;
            box-shadow: inset 0 0 0 1px #e5e7eb;
        }

        .action-item:nth-child(1) .action-icon {
            background: #eaf2ff;
        }

        .action-item:nth-child(2) .action-icon {
            background: #ecfdf3;
        }

        .action-item:nth-child(3) .action-icon {
            background: #ecfeff;
        }

        .action-icon svg {
            width: 34px;
            height: 34px;
        }

        .action-title {
            font-size: 15px;
            font-weight: bold;
            color: #111827;
            line-height: 1.3;
        }

        .footer-nav {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 1000;
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(12px);
    border-top: 1px solid #e5e7eb;
    padding: 10px 8px 14px;
}

.footer-nav-inner {
    max-width: 500px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 4px;
}

.nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 5px;
    color: #6b7280;
    padding: 8px 3px;
    border-radius: 14px;
    min-height: 62px;
    text-align: center;
    overflow: hidden;
}

.nav-item.active {
    background: #eaf2ff;
    color: #2563eb;
}

.nav-item svg {
    width: 22px;
    height: 22px;
    flex-shrink: 0;
}

.nav-label {
    font-size: 10px;
    font-weight: 600;
    line-height: 1.1;
    word-break: break-word;
    overflow-wrap: break-word;
    max-width: 100%;
}

        @media (max-width: 420px) {
            .header-title {
                font-size: 20px;
            }

            .welcome-fullname {
                font-size: 24px;
            }

            .balance-value {
                font-size: 30px;
            }

            .action-item {
                min-height: 118px;
                padding: 16px 8px 14px;
            }

            .action-icon {
                width: 56px;
                height: 56px;
            }

            .action-title {
                font-size: 14px;
            }
        }
    </style>
</head>
<body>

    <header class="header">
    <div class="header-logo">
    <img src="/static/images/logo.png" alt="FondAction Logo">
</div>

    <div class="header-nim">
        <span class="nim-label">NIM</span>
        <span class="nim-value">{{ member.nim }}</span>
    </div>
</header>

    <main class="page">
        <section class="welcome-box">
            <div class="welcome-label">Bienvenue</div>
            
            <div class="welcome-fullname">
                {{ member.last_name|default:"" }} {{ member.first_name|default:"" }}
            </div>
        </section>

        <section class="balance-card">
            <div class="balance-label">Montant total cotisé</div>
            <div class="balance-value">{{ total_contributions|default:"0.00" }} FCFA</div>

            <div class="balance-bottom">
                <p class="balance-text">
                    Votre contribution participe à bâtir notre avenir commun.
                    Merci de faire partie de cette communauté engagée.
                </p>
            </div>
        </section>

        <section class="actions-grid">
            <a href="/admins/member-payment/" class="action-item">
                <div class="action-icon">
                    <svg viewBox="-0.5 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M18 10.9199V2.91992" stroke="#2563eb" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                        <path d="M14.8008 6.11992L18.0008 2.91992L21.2008 6.11992" stroke="#2563eb" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                        <path d="M10.58 3.96997H6C4.93913 3.96997 3.92178 4.39146 3.17163 5.1416C2.42149 5.89175 2 6.9091 2 7.96997V17.97C2 19.0308 2.42149 20.0482 3.17163 20.7983C3.92178 21.5485 4.93913 21.97 6 21.97H18C19.0609 21.97 20.0783 21.5485 20.8284 20.7983C21.5786 20.0482 22 19.0308 22 17.97V13.8999" stroke="#2563eb" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                        <path d="M2 9.96997H5.37006C6.16571 9.96997 6.92872 10.286 7.49133 10.8486C8.05394 11.4112 8.37006 12.1743 8.37006 12.97C8.37006 13.7656 8.05394 14.5287 7.49133 15.0913C6.92872 15.6539 6.16571 15.97 5.37006 15.97H2" stroke="#2563eb" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                </div>
                <div class="action-title">Payer</div>
            </a>

            <a href="/admins/member-withdrawal/" class="action-item">
                <div class="action-icon">
                    <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" fill="#16a34a">
                        <path fill="#16a34a" d="M258 21.89c-.5 0-1.2 0-1.8.12-4.6.85-10.1 5.1-13.7 14.81-3.8 9.7-4.6 23.53-1.3 38.34 3.4 14.63 10.4 27.24 18.2 34.94 7.6 7.7 14.5 9.8 19.1 9 4.8-.7 10.1-5.1 13.7-14.7 3.8-9.64 4.8-23.66 1.4-38.35-3.5-14.8-10.4-27.29-18.2-34.94-6.6-6.8-12.7-9.22-17.4-9.22zM373.4 151.4c-11 .3-24.9 3.2-38.4 8.9-15.6 6.8-27.6 15.9-34.2 24.5-6.6 8.3-7.2 14.6-5.1 18.3 2.2 3.7 8.3 7.2 20 7.7 11.7.7 27.5-2.2 43-8.8 15.5-6.7 27.7-15.9 34.3-24.3 6.6-8.3 7.1-14.8 5-18.5-2.1-3.8-8.3-7.1-20-7.5-1.6-.3-3-.3-4.6-.3zm-136.3 92.9c-6.6.1-12.6.9-18 2.3-11.8 3-18.6 8.4-20.8 14.9-2.5 6.5 0 14.3 7.8 22.7 8.2 8.2 21.7 16.1 38.5 20.5 16.7 4.4 32.8 4.3 44.8 1.1 12.1-3.1 18.9-8.6 21.1-15 2.3-6.5 0-14.2-8.1-22.7-7.9-8.2-21.4-16.1-38.2-20.4-9.5-2.5-18.8-3.5-27.1-3.4zm160.7 58.1L336 331.7c4.2.2 14.7.5 14.7.5l6.6 8.7 54.7-28.5-14.2-10zm-54.5.1l-57.4 27.2c5.5.3 18.5.5 23.7.8l49.8-23.6-16.1-4.4zm92.6 10.8l-70.5 37.4 14.5 18.7 74.5-44.6-18.5-11.5zm-278.8 9.1a40.33 40.33 0 0 0-9 1c-71.5 16.5-113.7 17.9-126.2 17.9H18v107.5s11.6-1.7 30.9-1.8c37.3 0 103 6.4 167 43.8 3.4 2.1 10.7 2.9 19.8 2.9 24.3 0 61.2-5.8 69.7-9C391 452.6 494 364.5 494 364.5l-32.5-28.4s-79.8 50.9-89.9 55.8c-91.1 44.7-164.9 16.8-164.9 16.8s119.9 3 158.4-27.3l-22.6-34s-82.8-2.3-112.3-6.2c-15.4-2-48.7-18.8-73.1-18.8z"></path>
                    </svg>
                </div>
                <div class="action-title">Retrait</div>
            </a>

            <a href="/admins/member-transactions/" class="action-item">
                <div class="action-icon">
                    <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" fill="#0f766e">
                        <path d="M52,7H12a6,6,0,0,0-6,6V51a6,6,0,0,0,6,6H52a6,6,0,0,0,6-6V13A6,6,0,0,0,52,7Zm2,44a2,2,0,0,1-2,2H12a2,2,0,0,1-2-2V13a2,2,0,0,1,2-2H52a2,2,0,0,1,2,2Z"></path>
                        <path d="M45,29a2,2,0,0,0,0-4H22.83l2.58-2.59a2,2,0,0,0-2.82-2.82l-6,6a2,2,0,0,0-.44,2.18A2,2,0,0,0,18,29Z"></path>
                        <path d="M47,36H20a2,2,0,0,0,0,4H42.17l-2.58,2.59a2,2,0,1,0,2.82,2.82l6-6a2,2,0,0,0,.44-2.18A2,2,0,0,0,47,36Z"></path>
                    </svg>
                </div>
                <div class="action-title">Transactions</div>
            </a>
        </section>
    </main>

<nav class="footer-nav">
    <div class="footer-nav-inner">
        <a href="/admins/member-space/" class="nav-item active">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
            </svg>
            <div class="nav-label">Accueil</div>
        </a>

        <a href="/admins/member-card/" class="nav-item">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Zm6-10.125a1.875 1.875 0 1 1-3.75 0 1.875 1.875 0 0 1 3.75 0Zm1.294 6.336a6.721 6.721 0 0 1-3.17.789 6.721 6.721 0 0 1-3.168-.789 3.376 3.376 0 0 1 6.338 0Z" />
            </svg>
            <div class="nav-label">Carte</div>
        </a>

        <a href="/admins/member-infos/" class="nav-item">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="m11.25 11.25.041-.02a.75.75 0 0 1 1.063.852l-.708 2.836a.75.75 0 0 0 1.063.853l.041-.021M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9-3.75h.008v.008H12V8.25Z" />
            </svg>
            <div class="nav-label">Infos</div>
        </a>

        <a href="/admins/member-profile/" class="nav-item">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
            </svg>
            <div class="nav-label">Profil</div>
        </a>

        <a href="/admins/member-settings/" class="nav-item">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 0 1 1.37.49l1.296 2.247a1.125 1.125 0 0 1-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a7.723 7.723 0 0 1 0 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 0 1-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.47 6.47 0 0 1-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 0 1-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 0 1-1.369-.49l-1.297-2.247a1.125 1.125 0 0 1 .26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 0 1 0-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 0 1-.26-1.43l1.297-2.247a1.125 1.125 0 0 1 1.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28Z" />
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
            </svg>
            <div class="nav-label">Paramètres</div>
        </a>
    </div>
</nav>

</body>
</html>


<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Retrait</title>
    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #111827;
        }

        body {
            padding-top: 0;
            padding-bottom: 100px;
        }

        
        .simple-header {
    background: white;
    border-radius: 24px;
    padding: 22px 18px;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
    margin-bottom: 16px;
}

.simple-header h1 {
    margin: 0;
    font-size: 28px;
    font-weight: bold;
    color: #111827;
}

.back-btn {
    display: inline-block;
    margin-top: 12px;
    background: #111827;
    color: white;
    text-decoration: none;
    padding: 10px 16px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 600;
    transition: 0.2s ease;
}

.back-btn:hover {
    background: #000;
    transform: translateY(-1px);
}
       

.page {
    max-width: 520px;
    margin: 0 auto;
    padding: 18px 16px 0;
}

.info-card,
.form-card {
    background: white;
    border-radius: 24px;
    padding: 20px 16px;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
    margin-bottom: 16px;
}

.balance-box {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
    border-radius: 20px;
    padding: 18px;
}

.balance-label {
    font-size: 13px;
    color: rgba(255,255,255,0.75);
    margin-bottom: 8px;
}

.balance-value {
    font-size: 30px;
    font-weight: bold;
}

.field {
    margin-bottom: 14px;
}

.field label {
    display: block;
    font-weight: bold;
    margin-bottom: 6px;
    color: #111827;
}

.field input,
.field textarea {
    width: 100%;
    padding: 13px 14px;
    border: 1px solid #d1d5db;
    border-radius: 14px;
    font-size: 15px;
    outline: none;
}

.field textarea {
    min-height: 100px;
    resize: vertical;
}

.submit-btn {
    width: 100%;
    border: none;
    background: #16a34a;
    color: white;
    padding: 14px 16px;
    border-radius: 14px;
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
}

.submit-btn:hover {
    background: #15803d;
}

.msg {
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 14px;
    font-size: 14px;
    line-height: 1.6;
}

.msg-error {
    background: #fef2f2;
    color: #b91c1c;
    border: 1px solid #fecaca;
}

.msg-success {
    background: #f0fdf4;
    color: #166534;
    border: 1px solid #bbf7d0;
}

.warning-box {
    background: #fff7ed;
    border: 1px solid #fdba74;
    color: #9a3412;
    padding: 16px;
    border-radius: 16px;
    margin-bottom: 16px;
    font-size: 14px;
    line-height: 1.6;
}

.warning-box strong {
    display: block;
    margin-bottom: 8px;
    font-size: 15px;
}


    </style>
</head>
<body>

    

    <main class="page">

        <div class="simple-header">
    <h1>Retrait</h1>
    <a href="/admins/member-space/" class="back-btn"> Retour à l’espace membre</a>
    </div>

        


        


        <section class="info-card">
            <div class="balance-box">
                <div class="balance-label">Solde disponible</div>
                <div class="balance-value">{{ available_balance }} FCFA</div>
            </div>
        </section>


        <div class="warning-box">
    <strong>⚠️ Avertissement important</strong>
    <p>
        FondAction n’est pas seulement une plateforme, mais une communauté engagée vers des projets et avantages futurs destinés à ses membres. Ces opportunités vous seront communiquées en temps voulu.
        <br><br>
        Effectuer un retrait signifie réduire votre participation à cette dynamique collective.
        <br><br>
        Toute demande de retrait doit être faite avec sérieux.
        Une fois validée par l’administration, elle devient irréversible.
        <br><br>
        ⚠️ Toute demande inutile ou de test est fortement déconseillée :
        le montant pourra être prélevé sans garantie de transfert en cas d’erreur.
        <br><br>
        Avant de valider, assurez-vous que toutes les informations saisies sont correctes.
    </p>
</div>


        <section class="form-card">
            {% if error_message %}
                <div class="msg msg-error">{{ error_message }}</div>
            {% endif %}

            {% if success_message %}
                <div class="msg msg-success">{{ success_message }}</div>
            {% endif %}

            <form method="POST">
                {% csrf_token %}

                <div class="field">
                    <label>Montant</label>
                    <input type="number" name="amount" min="1" step="1" required>
                </div>

                <div class="field">
                    <label>Numéro qui va recevoir l'argent</label>
                    <input type="text" name="receiver_phone" required>
                </div>

                <div class="field">
                    <label>Motif</label>
                    <textarea name="reason" placeholder="Motif du retrait"></textarea>
                </div>

                <div class="field">
                    <label>Code PIN</label>
                    <input type="password" name="pin" maxlength="5" autocomplete="new-password" inputmode="numeric" required>
                </div>

                <button type="submit" class="submit-btn">Valider la demande</button>
            </form>
        </section>
    </main>

</body>
</html>