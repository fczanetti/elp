from django.urls import path
from engplat.podcasts import views

app_name = 'podcasts'
urlpatterns = [
    path('', views.indice_podcasts, name='indice'),
    path('<slug:slug>', views.detalhe_podcast, name='detalhe'),
]
