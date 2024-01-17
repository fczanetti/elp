import pytest
from django.urls import reverse

from engplat.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    """
    Cria uma requisição na home page e retorna sua resposta.
    :return:
    """
    resposta = client.get(reverse('base:home'))
    return resposta


def test_status_code_home(resp):
    """
    Certifica de que a requisição foi concluída com sucesso (status code da resp == 200).
    """
    assert resp.status_code == 200


def test_link_home_navbar(resp):
    """
    Certifica de que a navbar contém um link direcionando para a home page.
    """
    assert_contains(resp, f'href="{reverse("base:home")}"')


def test_cont_adic_podcast(resp):
    """
    Certifica de que existe o conteúdo adicional Podcasts na home page.
    """
    assert_contains(resp, '<h2>Podcasts</h2>')


def test_links_redes_sociais(resp):
    """
    Certifica de que o link para o canal do Youtube está presente na home page.
    """
    assert_contains(resp, 'href="https://www.youtube.com/@adiadi8803"')


def test_link_podcasts(resp):
    """
    Certifica de que o link do conteúdo adicional Podcasts está presente na home page.
    """
    assert_contains(resp, f'href="{reverse("podcasts:indice")}"')
