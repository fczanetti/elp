from django.urls import path
from engplat.modulos import views

app_name = 'modulos'
urlpatterns = [
    path('', views.indice_modulos, name='indice_modulos'),
    path('<slug:slug>', views.detalhe_modulo, name='detalhe_modulo'),
    path('<slug:modulo_slug>/<slug:slug>', views.detalhe_aula, name='detalhe_aula'),
]
