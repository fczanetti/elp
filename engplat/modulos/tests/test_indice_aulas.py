import pytest
from django.urls import reverse
from model_bakery import baker

from engplat.django_assertions import assert_contains


@pytest.fixture
def modulo(db):
    mod = baker.make('Modulo')
    # aulas = baker.make('Aula', modulo=mod, _quantity=3)
    mod.aula_set.set(baker.make('Aula', modulo=mod, _quantity=3))
    return mod


@pytest.fixture
def resp(client, modulo):
    return client.get(reverse('modulos:detalhe_modulo', args=(modulo.slug,)))


def test_status_code_aulas_modulo(resp):
    assert resp.status_code == 200


def test_titulo_modulo(resp, modulo):
    assert_contains(resp, modulo.titulo)


def test_descricao_modulo(resp, modulo):
    assert_contains(resp, modulo.descricao)


def test_publico_modulo(resp, modulo):
    assert_contains(resp, modulo.publico)


def test_aulas_modulo(resp, modulo):
    for aula in modulo.aula_set.all():
        assert_contains(resp, aula.titulo)
