from django.urls import reverse
from engplat.django_assertions import assert_contains


def test_status_code(resp_indice_podcasts):
    """
    Certifica de que a requisição foi bem sucedida e a resposta retornou com status code = 200.
    """
    assert resp_indice_podcasts.status_code == 200


def test_titulo_conteudo_principal(resp_indice_podcasts):
    """
    Certifica de que o título do conteúdo principal está presente (Podcasts).
    """
    assert_contains(resp_indice_podcasts, 'Podcasts')


def test_lista_de_podcasts(resp_indice_podcasts, podcasts_indice):
    """
    Certifica que que o título de cada podcast criado está presente na página de índice.
    :param podcasts: Podcasts que devem ser listados na página.
    """
    for podcast in podcasts_indice:
        assert_contains(resp_indice_podcasts, f'{podcast.titulo}')


def test_links_detalhe_podcasts(resp_indice_podcasts, podcasts_indice):
    """
    Certifica que o link que leva para a página de detalhes de cada podcast está presente na página de índice.
    :param podcasts: Podcasts que devem aparecer na página.
    """
    for podcast in podcasts_indice:
        assert_contains(resp_indice_podcasts, f'href="{reverse("podcasts:detalhe", args=(podcast.slug,))}"')


def test_tiulo_pagina_podcasts_breadcrumb(resp_indice_podcasts):
    """
    Certifica de que o titulo da pagina de podcasts está presente no breadcrumb.
    """
    assert_contains(resp_indice_podcasts, '<li class="breadcrumb-item active" aria-current="page">Podcasts</li>')


def test_link_home_breadcrumb(resp_indice_podcasts):
    """
    Certifica de que o link para a home page está presente no breadcrumb.
    """
    assert_contains(resp_indice_podcasts, f'<li class="breadcrumb-item"><a class="text-decoration-none" '
                                          f'href="{reverse("base:home")}">Home</a></li>')
