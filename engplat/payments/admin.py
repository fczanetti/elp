from django.contrib import admin
from engplat.payments.models import UserPayment, Product
from ordered_model.admin import OrderedModelAdmin


@admin.register(UserPayment)
class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_bool', 'product', 'stripe_checkout_id', 'created_at', 'updated_at']


@admin.register(Product)
class ProductAdmin(OrderedModelAdmin):
    list_display = ['prod_name', 'num_avail_days', 'available', 'description', 'slug', 'stripe_id']
    prepopulated_fields = {'slug': ['prod_name']}
