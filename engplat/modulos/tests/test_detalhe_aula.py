from engplat.django_assertions import assert_contains


def test_status_code_detalhe_aula(resp_detalhe_aula):
    """
    Certifica de que a requisição para a página de detalhes da aula foi retornada com sucesso.
    :return: Resposta da requisição gerada.
    """
    assert resp_detalhe_aula.status_code == 200


def test_titulo_aula(resp_detalhe_aula, aula):
    """
    Certifica de que o título da aula está presente na página de detalhes da aula.
    :param aula: Aula utilizada para gerar a requisição/renderizar a página.
    """
    assert_contains(resp_detalhe_aula, aula.titulo)


def test_descricao_aula(resp_detalhe_aula, aula):
    """
    Certifica de que a descrição da aula está presente na página de detalhes desta.
    """
    assert_contains(resp_detalhe_aula, aula.descricao)


def test_id_plataforma_aula(resp_detalhe_aula, aula):
    """
    Certifica de que o ID que direciona o link para o vídeo na plataforma (Youtube) está presente na página de detalhes
    da aula.
    """
    assert_contains(resp_detalhe_aula, aula.plat_id)
