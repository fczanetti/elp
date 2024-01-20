from django.urls import path
from engplat.base import views

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
]
