from django.db import models
from django.utils import timezone

from tests.models import TestOrder
from diagnostic_centers.models import DiagnosticAdmin, DiagnosticStaff


class OrderValidation(models.Model):

    PAYMENT_STATUS = (
        ('Full Payment Complete', 'Full Payment Complete'),
        ('Payment NOT Complete', 'Payment NOT Complete'),
    )

    approved_order_by_client = models.ForeignKey(TestOrder, on_delete=models.DO_NOTHING)

    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS)
    confirmed_by_staff = models.BooleanField(blank=False)
    confirmation_datetime = models.DateTimeField(default=timezone.now)

    staff = models.ForeignKey(DiagnosticStaff, on_delete=models.DO_NOTHING, blank=True, null=True)
    admin = models.ForeignKey(DiagnosticAdmin, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.payment_status


# class Reports(models.Model):
#
#     confirmed_orders_for_report = models.ForeignKey(OrderValidation, on_delete=models.CASCADE)
#
#     upload_reports = models.FileField(upload_to='report_docs')
#     send_report =
#     report_sending_datetime =
#     report_sent_status = models.BooleanField()
#
#     class Meta:
#         ordering = ['-id']
#
#     def __str__(self):
#         return self.confirmed_orders_for_report.approved_orders.client_info.user.username

