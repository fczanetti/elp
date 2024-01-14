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
    modulos = [baker.make('Modulo', order=ord) for ord in [2, 0, 3, 1]]
    return modulos


def test_facade_listar_modulos_ordenados(modulos):
    """
    Aqui uma lista de módulos não ordenaods é recebida e ordenada, e esta é comparada com o resultado da função
    que lista os módulos de maneira ordenada.
    :param modulos:
    :return:
    """
    modulos.sort(key=lambda mod: mod.order)
    mod_ord = list(facade.listar_modulos_ordenados())
    assert mod_ord == modulos
