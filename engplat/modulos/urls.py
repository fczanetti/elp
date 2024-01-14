from django.urls import path
from engplat.modulos import views

app_name = 'modulos'
urlpatterns = [
    path('', views.indice_modulos, name='indice_modulos')
]
