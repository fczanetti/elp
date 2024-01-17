from engplat.podcasts import facade


def test_listar_podcasts_ordenados(podcasts_datas_especificas):
    """
    Certifica de que a função definida no módulo facade.py está ordenando corretamente os módulos ao buscar no banco
    de dados.
    """
    assert (list(sorted(podcasts_datas_especificas, key=lambda pod: pod.data_gravacao, reverse=True)) ==
            facade.buscar_podcasts_ordenados())
