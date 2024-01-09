import pytest
from django.urls import reverse

from engplat.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resposta = client.get(reverse('base:home'))
    return resposta


def test_status_code_home(resp):
    assert resp.status_code == 200


def test_link_home_navbar(resp):
    assert_contains(resp, f'href="{reverse("base:home")}"')


def test_cont_adic_podcast(resp):
    assert_contains(resp, '<h2>Podcasts</h2>')


def test_cont_adic_lev_test(resp):
    assert_contains(resp, '<h2>Leveling test</h2>')


def test_links_redes_sociais(resp):
    assert_contains(resp, 'href="https://www.youtube.com/@adiadi8803"')


def test_link_podcasts(resp):
    assert_contains(resp, f'href="{reverse("podcasts:indice")}"')
