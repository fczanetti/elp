from django.contrib import admin
from engplat.payments.models import UserPayment


@admin.register(UserPayment)
class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_bool', 'stripe_checkout_id']
