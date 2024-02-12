from django.urls import path
from engplat.payments import views


app_name = 'payments'
urlpatterns = [
    path('product_page', views.product_page, name='product_page'),
    path('return_page', views.return_page, name='return_page'),
    path('session_status', views.session_status, name='session_status'),
    path('stripe_webhook', views.stripe_webhook, name='stripe_webhook')
]
