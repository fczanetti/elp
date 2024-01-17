from engplat.modulos import facade


def test_facade_listar_modulos_ordenados(modulos_desordenados):
    """
    Aqui uma lista de módulos não ordenaods é recebida e ordenada, e esta é comparada com o resultado da função
    que lista os módulos de maneira ordenada.
    """
    modulos_desordenados.sort(key=lambda mod: mod.order)
    mod_ord = list(facade.listar_modulos_ordenados())
    assert mod_ord == modulos_desordenados


def test_facade_buscar_aulas_ordenadas(modulo, aulas):
    """
    Ordena as aulas criadas pela fixture através do campo 'order'(django-ordered-models) e compara as aulas ordenadas
    através da função definida em facade.py. Se as listas comparadas forem iguais (mesma ordem) o teste é validado.
    """
    aulas.sort(key=lambda aula: aula.order)
    aulas_ord = list(facade.listar_aulas_de_modulo_ordenadas(modulo))
    assert aulas == aulas_ord
