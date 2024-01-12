from engplat.podcasts.models import Podcast


def buscar_podcasts_ordenados():
    """
    Busca os podcasts no banco de dados e os ordena de forma reversa pela data de gravação.
    :return: Lista de podcasts ordenados reversamente por data de gravação.
    """
    pods = Podcast.objects.order_by('-data_gravacao').all()
    return list(pods)
