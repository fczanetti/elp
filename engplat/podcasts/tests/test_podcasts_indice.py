import pytest
from django.urls import reverse
from engplat.django_assertions import assert_contains
from model_bakery import baker
from engplat.podcasts.models import Podcast


@pytest.fixture
def podcasts(db):
    pods = baker.make(Podcast, _quantity=3)
    return pods


@pytest.fixture
def resp(client, podcasts):
    return client.get(reverse('podcasts:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_conteudo_principal(resp):
    assert_contains(resp, '<h1>Podcasts</h1>')


def test_lista_de_podcasts(resp, podcasts):
    for podcast in podcasts:
        assert_contains(resp, f'{podcast.titulo}')
