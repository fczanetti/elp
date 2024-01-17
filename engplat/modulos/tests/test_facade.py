import pytest
from model_bakery import baker
from engplat.modulos import facade


@pytest.fixture
def modulos(db):
    """
    Esta função cria módulos não ordenados para que sejam ordenados pela função no módulo facade.py.
    :param db:
    :return: lista de módulos não ordenados.
    """
    modulos = [baker.make('Modulo', order=v) for v in [2, 0, 3, 1]]
    return modulos


@pytest.fixture
def modulo(db):
    """
    Cria um módulo.
    :param db:
    :return: módulo criado.
    """
    return baker.make('Modulo')


@pytest.fixture
def aulas(modulo):
    """
    Cria aulas de forma desordenada para que sejam ordenadas e comparadas com o resultado da função que busca e ordena.
    :param modulo: Módulo para o qual as aulas serão criadas.
    :return: Lista de aulas desordenada.
    """
    aulas = [baker.make('Aula', modulo=modulo, order=v) for v in [2, 1, 3]]
    return aulas


def test_facade_listar_modulos_ordenados(modulos):
    """
    Aqui uma lista de módulos não ordenaods é recebida e ordenada, e esta é comparada com o resultado da função
    que lista os módulos de maneira ordenada.
    """
    modulos.sort(key=lambda mod: mod.order)
    mod_ord = list(facade.listar_modulos_ordenados())
    assert mod_ord == modulos


def test_facade_buscar_aulas_ordenadas(modulo, aulas):
    """
    Ordena as aulas criadas pela fixture através do campo 'order'(django-ordered-models) e compara as aulas ordenadas
    através da função definida em facade.py. Se as listas comparadas forem iguais (mesma ordem) o teste é validado.
    """
    aulas.sort(key=lambda aula: aula.order)
    aulas_ord = list(facade.listar_aulas_de_modulo_ordenadas(modulo))
    assert aulas == aulas_ord
