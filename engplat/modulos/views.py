from django.shortcuts import render
from engplat.modulos import facade


def indice_modulos(request):
    modulos = facade.listar_modulos_ordenados()
    return render(request, 'modulos/indice_modulos.html', {'modulos': modulos})


def detalhe_modulos(request):
    return render(request, 'modulos/detalhe.html')
