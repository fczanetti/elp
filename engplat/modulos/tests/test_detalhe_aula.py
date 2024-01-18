from engplat.django_assertions import assert_contains
from django.urls import reverse


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


def test_titulo_aula_breadcrumb(resp_detalhe_aula, aula):
    """
    Certifica de que o título da aula está presente no breadcrumb.
    """
    assert_contains(resp_detalhe_aula, f'<li class="breadcrumb-item active" aria-current="page">{aula.titulo}</li>')


def test_titulo_modulo_breadcrumb(resp_detalhe_aula, aula):
    """
    Certifica de que o título do modulo está presente no breadcrumb.
    """
    assert_contains(resp_detalhe_aula, f'<li class="breadcrumb-item"><a class="text-decoration-none" '
                                       f'href="{aula.modulo.get_absolute_url()}">{aula.modulo.titulo}</a></li>')


def test_indice_modulos_breadcrumb(resp_detalhe_aula, aula):
    """
    Certifica de que o índice dos modulos está presente no breadcrumb.
    """
    assert_contains(resp_detalhe_aula, f'<li class="breadcrumb-item"><a class="text-decoration-none" '
                                       f'href="{reverse("modulos:indice_modulos")}">Módulos</a></li>')


def test_link_home_breadcrumb(resp_detalhe_aula, aula):
    """
    Certifica de que o link para a home page está presente no breadcrumb.
    """
    assert_contains(resp_detalhe_aula, f'<li class="breadcrumb-item"><a '
                                       f'class="text-decoration-none" href="{reverse("base:home")}">Home</a></li>')
