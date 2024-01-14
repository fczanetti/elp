from django.shortcuts import render
from engplat.modulos.models import Modulo


def indice_modulos(request):
    modulos = Modulo.objects.all()
    return render(request, 'modulos/indice_modulos.html', {'modulos': modulos})


def detalhe_modulos(request):
    return render(request, 'modulos/detalhe.html')
