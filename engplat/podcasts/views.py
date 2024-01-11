from django.shortcuts import render, get_object_or_404
from engplat.podcasts.models import Podcast


def indice_podcasts(request):
    podcasts = Podcast.objects.all()
    return render(request, 'podcasts/indice_podcasts.html', context={'podcasts': podcasts})


def detalhe_podcast(request, slug):
    podcast = get_object_or_404(Podcast, slug=slug)
    return render(request, 'podcasts/detalhe_podcast.html', context={'podcast': podcast})
