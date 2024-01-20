from django.shortcuts import render
from django.contrib.auth.views import LoginView


def home(request):
    return render(request, 'base/home.html')


class UserLoginView(LoginView):
    template_name = 'registration/user_login.html'
    next_page = '/'
