import pytest
from django.urls import reverse

from engplat.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('modulos:indice_modulos'))


def test_status_code_indice_modulo(resp):
    assert resp.status_code == 200


def test_titulo_indice_modulos(resp):
    assert_contains(resp, '<title>Módulos - Índice</title>')
