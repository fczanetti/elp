from django.urls import path
from engplat.base import views
from engplat.base.views import CustomPasswordResetView, CustomPasswordChangeView

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
]
