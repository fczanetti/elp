from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordChangeView,
    LogoutView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.contrib import messages

from engplat.base.forms import MyUserCreationForm, FileModelForm


def home(request):
    return render(request, 'base/home.html')


class UserLoginView(LoginView):
    template_name = 'registration/user_login.html'
    next_page = '/'


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    success_url = '/accounts/password_reset_confirmed'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = '/accounts/password_alterado'


class UserLogoutView(LogoutView):
    next_page = '/'


def password_alterado(request):
    return render(request, 'registration/password_alterado.html')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done_custom.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm_custom.html'
    success_url = '/accounts/password_reset_finished'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_finish.html'


def user_creation(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('base:user_created'))
        else:
            return render(request, 'registration/user_creation.html', {'form': form})
    else:
        form = MyUserCreationForm()
        return render(request, 'registration/user_creation.html', {'form': form})


def user_created(request):
    return render(request, 'registration/user_created.html')


def files(request):
    if request.method == "POST":
        form = FileModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Arquivo salvo com sucesso.")

    form = FileModelForm()
    return render(request, "base/files.html", {"form": form})
