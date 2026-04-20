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