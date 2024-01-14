import pytest
from django.urls import reverse
from engplat.django_assertions import assert_contains
from model_bakery import baker


@pytest.fixture
def modulos(db):
    modulos = baker.make('Modulo', _quantity=3)
    return modulos


@pytest.fixture
def resp(client, modulos):
    return client.get(reverse('modulos:indice_modulos'))


def test_status_code_indice_modulo(resp):
    assert resp.status_code == 200


def test_titulo_indice_modulos(resp):
    assert_contains(resp, '<title>Módulos - Índice</title>')


def test_titulos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_publico_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.publico)


def test_descricao_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.descricao)


def test_link_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, reverse('modulos:detalhe', args=(modulo.slug,)))
