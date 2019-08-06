from django.db import models
from django.utils import timezone

from diagnostic_centers.models import DiagnosticCenter
from custom_users.models import Profile


class TestCategory(models.Model):
    category_name = models.CharField(max_length=50)
    center = models.ForeignKey(DiagnosticCenter, on_delete=models.CASCADE, related_name='category_center',
                               null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Test Categories'
        ordering = ['-id']

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

    PAYMENT_TYPE = (
        ('Full Payment', 'Full Payment'),
        ('Half Payment', 'Half Payment'),
    )

    PAYMENT_METHOD = (
        ('BKASH', 'Bkash'),
        ('CREDIT CARD', 'Credit Card'),
        ('ON SPOT', 'On Spot'),
    )

    TIME_SLOT = (
        ('10:00 AM - 2:00 PM', '10:00 AM - 2:00 PM'),
        ('3:00 PM - 7:00 PM', '3:00 PM - 7:00 PM'),
        ('8:00 PM - 10:00 PM', '8:00 PM - 10:00 PM'),
    )

    client_info = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='test_user_order')
    contact_no = models.CharField(max_length=20, blank=False, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    test_info = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True, related_name='test_order')

    # Step 3+4+5+6
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE, default='Full Payment', blank=True, null=True)

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, blank=True, null=True)
    booked_time_slot = models.CharField(max_length=20, choices=TIME_SLOT, blank=True, null=True)
    booked_date = models.DateField(blank=True, null=True)
    order_created_at = models.TimeField(auto_now=True)

    # for all steps
    staff_check = models.BooleanField(default=False)

    admin_approve = models.BooleanField(default=False)
    order_confirmed = models.BooleanField(default=False)

    # for all steps
    accepted = models.BooleanField(default=False)

    # Step 4+5+6
    validation = models.BooleanField(default=False)

    # Step 2
    came_for_test = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Test Orders'

    # ToDo: Solve object name ERROR (linked to 'PaymentValidation' model)
    def __str__(self):
        return self.test_info.test_name






