import pytest
from django.urls import reverse
from engplat.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('podcasts:podcasts'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_conteudo_principal(resp):
    assert_contains(resp, '<h1>Podcasts</h1>')
