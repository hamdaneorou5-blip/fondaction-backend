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