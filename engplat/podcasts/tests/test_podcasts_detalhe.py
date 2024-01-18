from engplat.django_assertions import assert_contains
from django.urls import reverse


def test_podcast_inexistente(resp_podcast_inexistente):
    """
    Certifica de que o erro 404 é apresentado ao tentar acessar uma página cujo podcast não está cadastrado no banco
    (preenchendo a URL manualmente).
    """
    assert resp_podcast_inexistente.status_code == 404


def test_status_code_detalhe_podcast(resp_detalhe_podcast):
    """
    Certifica de que a requisição é bem sucedida e a resposta retorna com status code = 200.
    """
    assert resp_detalhe_podcast.status_code == 200


def test_titulo_podcast(resp_detalhe_podcast, podcast_detalhe):
    """
    Certifica de que o título do podcast está presente em sua página de detalhes.
    """
    assert_contains(resp_detalhe_podcast, f'{podcast_detalhe.titulo}')


def test_url_podcast_detalhe(resp_detalhe_podcast, podcast_detalhe):
    """
    Certifica de que a URL que liga o podcast com a plataforma do Youtube está presente na página de detalhe do podcast.
    """
    assert_contains(resp_detalhe_podcast, f'https://www.youtube.com/embed/{podcast_detalhe.plat_id}')


def test_descricao_podcast(resp_detalhe_podcast, podcast_detalhe):
    """
    Certifica de que a descrição do podcast está presente em sua página de detalhes.
    """
    assert_contains(resp_detalhe_podcast, f'{podcast_detalhe.descricao}')


def test_titulo_podcast_breadcrumb(resp_detalhe_podcast, podcast_detalhe):
    """
    Certifica de que o título do podcast está presente no breadcrumb.
    """
    assert_contains(resp_detalhe_podcast, f'<li class="breadcrumb-item active" '
                                          f'aria-current="page">{podcast_detalhe.titulo}</li>')


def test_indice_podcasts_breadcrumb(resp_detalhe_podcast):
    """
    Certifica de que o link para o índice de podcasts está presente no breadcrumb.
    """
    assert_contains(resp_detalhe_podcast, f'<li class="breadcrumb-item"><a class="text-decoration-none" '
                                          f'href="{reverse("podcasts:indice")}">Podcasts</a></li>')


def test_link_home_breadcrumb(resp_detalhe_podcast):
    """
    Certifica de que o link para a home page está presente no breadcrumb.
    """
    assert_contains(resp_detalhe_podcast, f'<li class="breadcrumb-item"><a '
                                          f'class="text-decoration-none" href="{reverse("base:home")}">Home</a></li>')
