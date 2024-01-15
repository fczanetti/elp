from django.shortcuts import render
from engplat.modulos import facade


def indice_modulos(request):
    modulos = facade.listar_modulos_ordenados()
    return render(request, 'modulos/indice_modulos.html', {'modulos': modulos})


def detalhe_modulo(request, slug):
    modulo = facade.buscar_modulo(slug)
    aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/detalhe_modulo.html', {'modulo': modulo, 'aulas': aulas})
