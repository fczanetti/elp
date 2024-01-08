from django.shortcuts import render


def podcasts(request):
    return render(request, 'podcasts/podcasts.html')
