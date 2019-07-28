from django.db import models

from tests.models import TestOrder


class PaymentValidation(models.Model):

    # category = models.OneToOneField(TestOrder, on_delete=models.SET_NULL, null=True)
    approved_order = models.OneToOneField(TestOrder, on_delete=models.SET_NULL, null=True)

    upload_report = models.FileField(upload_to='reports_PDF', null=True, blank=True)

    send_message = models.CharField(max_length=250, null=True, blank=True)

    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    # ToDo: Solve object name ERROR (linked to 'TestOrder' model)
    def __str__(self):
        return self.approved_order.test_info.test_name
        # return self.send_message



