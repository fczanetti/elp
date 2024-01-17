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
def modulo_sem_aulas(db):
    """
    Cria um módulo sem aulas para teste de mensagem de aulas não cadastradas.
    """
    return baker.make('Modulo')


@pytest.fixture
def resp_modulo_sem_aulas(client, modulo_sem_aulas):
    # return client.get(reverse('modulos:detalhe_modulo', args=(modulo_sem_aulas.slug,)))
    return client.get(modulo_sem_aulas.get_absolute_url())


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


def test_titulo_aulas_modulo(resp, modulo):
    for aula in modulo.aula_set.all():
        assert_contains(resp, aula.titulo)


def test_link_aulas_modulo(resp, modulo):
    for aula in modulo.aula_set.all():
        assert_contains(resp, reverse('modulos:detalhe_aula', kwargs={'modulo_slug': modulo.slug,
                                                                      'slug': aula.slug}))


def test_modulo_sem_aulas(resp_modulo_sem_aulas, modulo_sem_aulas):
    assert_contains(resp_modulo_sem_aulas, '<li>Não há aulas cadastradas.</li>')
