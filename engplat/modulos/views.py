from django.shortcuts import render


def indice_modulos(request):
    return render(request, 'modulos/indice_modulos.html')
