from django.db import models
from django.utils import timezone

from diagnostic_centers.models import DiagnosticCenter
from custom_users.models import Profile


class TestCategory(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Test Categories'

    def __str__(self):
        return self.category_name


class Test(models.Model):

    ACTIVE_STATUS = (
        ('Available', 'AVAILABLE'),
        ('Closed', 'CLOSED'),
    )

    test_name = models.CharField(max_length=250, blank=False)
    image = models.ImageField(default='default_test.jpg', upload_to='test_pics')
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE, related_name='test_category')
    center = models.ForeignKey(DiagnosticCenter, on_delete=models.CASCADE, related_name='test_center')
    discount = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    active_status = models.CharField(max_length=20, choices=ACTIVE_STATUS, default='AVAILABLE')

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Tests'

    def __str__(self):
        return self.test_name


class TestOrder(models.Model):

    PAYMENT_OPTION = (
        ('Full Payment', 'Full Payment'),
        ('Half Payment', 'Half Payment'),
    )

    client_info = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='test_user_order')
    contact_no = models.CharField(max_length=20, blank=False, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    test_info = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_order')
    payment_option = models.CharField(max_length=20, choices=PAYMENT_OPTION, blank=False)
    date = models.DateTimeField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    staff_check = models.BooleanField(default=False)
    admin_approve = models.BooleanField(default=False)

    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Test Orders'

    def __str__(self):
        return self.client_info.user.username






