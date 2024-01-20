from django.shortcuts import render
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, LogoutView


def home(request):
    return render(request, 'base/home.html')


class UserLoginView(LoginView):
    template_name = 'registration/user_login.html'
    next_page = '/'


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = '/accounts/password_alterado'


class UserLogoutView(LogoutView):
    next_page = '/'


def password_alterado(request):
    return render(request, 'registration/password_alterado.html')
