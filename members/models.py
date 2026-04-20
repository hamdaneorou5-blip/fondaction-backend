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
        ('adjustment', 'Ajustement'),
    ]

    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('success', 'Succès'),
        ('failed', 'Échoué'),
        ('cancelled', 'Annulé'),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reference = models.CharField(max_length=100, unique=True)
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
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    receiver_account = models.CharField(max_length=100)
    account_holder_name = models.CharField(max_length=255)
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

    def __str__(self):
        return f"Retrait {self.member.nim} - {self.amount} - {self.status}"


class InfoPost(models.Model):
    POST_TYPE_CHOICES = [
        ('text', 'Texte'),
        ('image', 'Image'),
        ('video', 'Vidéo'),
        ('mixed', 'Mixte'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    post_type = models.CharField(max_length=20, choices=POST_TYPE_CHOICES, default='text')
    image = models.ImageField(upload_to='members/info_posts/images/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='members/projects/pdfs/')
    cover_image = models.ImageField(upload_to='members/projects/covers/', null=True, blank=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OfficialContract(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='members/contracts/official/')
    version = models.CharField(max_length=50, default='1.0')
    is_active = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - v{self.version}"


class MemberContractSubmission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('approved', 'Approuvé'),
        ('rejected', 'Rejeté'),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='contract_submissions'
    )
    contract = models.ForeignKey(
        OfficialContract,
        on_delete=models.CASCADE,
        related_name='submissions'
    )
    signed_file = models.FileField(upload_to='members/contracts/signed/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_note = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.member.nim} - {self.contract.title} - {self.status}"


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