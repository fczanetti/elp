from django.shortcuts import render
from engplat.modulos import facade
from engplat.modulos.models import Aula
from django.contrib.auth.decorators import login_required


@login_required
def indice_modulos(request):
    modulos = facade.listar_modulos_ordenados()
    return render(request, 'modulos/indice_modulos.html', {'modulos': modulos})


@login_required
def detalhe_modulo(request, slug):
    modulo = facade.buscar_modulo(slug)
    aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/detalhe_modulo.html', {'modulo': modulo, 'aulas': aulas})


@login_required
def detalhe_aula(request, slug, modulo_slug):
    aula = Aula.objects.select_related('modulo').get(slug=slug)
    return render(request, 'modulos/detalhe_aula.html', {'aula': aula})
