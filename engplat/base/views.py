from django.shortcuts import render
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView


def home(request):
    return render(request, 'base/home.html')


class UserLoginView(LoginView):
    template_name = 'registration/user_login.html'
    next_page = '/'


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
