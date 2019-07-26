from django.contrib import admin

from .models import PaymentValidation


class PaymentValidationAdmin(admin.ModelAdmin):
    list_display = ['id', 'approved_order', 'datetime', 'upload_report', 'send_message']
    list_editable = ['send_message']
    # list_display_links = ['approved_order']


admin.site.register(PaymentValidation, PaymentValidationAdmin)



