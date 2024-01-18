from django.urls import reverse
from engplat.django_assertions import assert_contains


def test_status_code_indice_modulo(resp_indice_modulos):
    """
    Certifica de que a resposta da requisição para a página de índice de módulos foi retornada com sucesso.
    """
    assert resp_indice_modulos.status_code == 200


def test_titulo_indice_modulos(resp_indice_modulos):
    """
    Certifica de que o título da página está presente na resposta da requisição.
    """
    assert_contains(resp_indice_modulos, '<title>Módulos - Índice</title>')


def test_titulos_modulos(resp_indice_modulos, modulos_desordenados):
    """
    Certifica de que o título de cada módulo criado está presente na página de índice de módulos.
    :param modulos: módulos criados que devem aparecer na página.
    """
    for modulo in modulos_desordenados:
        assert_contains(resp_indice_modulos, modulo.titulo)


def test_publico_modulos(resp_indice_modulos, modulos_desordenados):
    """
    Certifica de que o público de cada módulo está presente na página de índice de módulos.
    """
    for modulo in modulos_desordenados:
        assert_contains(resp_indice_modulos, modulo.publico)


def test_descricao_modulos(resp_indice_modulos, modulos_desordenados):
    """
    Certifica de que a descrição de cada módulo está presente na página de índice de módulos.
    """
    for modulo in modulos_desordenados:
        assert_contains(resp_indice_modulos, modulo.descricao)


def test_link_modulos(resp_indice_modulos, modulos_desordenados):
    """
    Certifica de que os links que direcionam para o detalhe de cada módulo está presente na página de índice de módulos.
    """
    for modulo in modulos_desordenados:
        assert_contains(resp_indice_modulos, reverse('modulos:detalhe_modulo', args=(modulo.slug,)))


def test_titulo_modulo_breadcrumb(resp_indice_modulos):
    """
    Certifica de que o título da página de módulos está presente no breadcrumb.
    """
    assert_contains(resp_indice_modulos, '<li class="breadcrumb-item active" aria-current="page">Modulos</li>')


def test_link_home_breadcrumb(resp_indice_modulos):
    """
    Certifica de que o link da home page está presente no breadcrumb.
    """
    assert_contains(resp_indice_modulos, f'<li class="breadcrumb-item"><a class="text-decoration-none" '
                                         f'href="{reverse("base:home")}">Home</a></li>')
