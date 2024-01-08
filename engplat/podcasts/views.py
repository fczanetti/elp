from django.shortcuts import render
from engplat.podcasts.models import Podcast


def podcasts(request):
    podcasts = Podcast.objects.all()
    return render(request, 'podcasts/podcasts.html', context={'podcasts': podcasts})
