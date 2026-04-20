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