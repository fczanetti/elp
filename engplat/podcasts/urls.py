from django.urls import path
from engplat.podcasts import views

app_name = 'podcasts'
urlpatterns = [
    path('', views.podcasts, name='podcasts')
]
