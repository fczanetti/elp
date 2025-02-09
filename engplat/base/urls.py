from django.urls import path
from engplat.base import views

app_name = "base"
urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/login/", views.UserLoginView.as_view(), name="login"),
    path("accounts/logout/", views.UserLogoutView.as_view(), name="logout"),
    path("accounts/password_reset/", views.CustomPasswordResetView.as_view(), name="password_reset"),
    path("accounts/password_change/", views.CustomPasswordChangeView.as_view(), name="password_change"),
    path("accounts/password_alterado", views.password_alterado, name="password_alterado"),
    path("accounts/password_reset_confirmed", views.CustomPasswordResetDoneView.as_view(),
         name="password_reset_confirmed"),
    path("accounts/reset/<uidb64>/<token>/", views.CustomPasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path("accounts/password_reset_finished", views.CustomPasswordResetCompleteView.as_view(),
         name="password_reset_finished"),
    path("accounts/user_creation", views.user_creation, name="user_creation"),
    path("accounts/user_created", views.user_created, name="user_created"),
    path("files", views.files, name="files"),
]
