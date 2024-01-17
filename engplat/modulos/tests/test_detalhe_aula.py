import pytest
from model_bakery import baker
from django.urls import reverse

from engplat.django_assertions import assert_contains


@pytest.fixture
def modulo(db):
    return baker.make('Modulo')


@pytest.fixture
def aula(modulo):
    return baker.make('Aula', modulo=modulo, descricao='Descrição de aula')


@pytest.fixture
def resp(client, aula):
    return client.get(reverse('modulos:detalhe_aula', kwargs={'slug': aula.slug,
                                                              'modulo_slug': aula.modulo.slug}))


def test_status_code_detalhe_aula(resp):
    assert resp.status_code == 200


def test_titulo_aula(resp, aula):
    assert_contains(resp, aula.titulo)


def test_descricao_aula(resp, aula):
    assert_contains(resp, aula.descricao)


def test_id_plataforma_aula(resp, aula):
    assert_contains(resp, aula.plat_id)
