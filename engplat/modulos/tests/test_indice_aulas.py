from django.urls import reverse
from engplat.django_assertions import assert_contains


def test_status_code_aulas_modulo(resp_detalhe_modulo):
    """
    Certifica de que a resposta da requisição para a página de detalhes de módulo foi gerada com sucesso.
    """
    assert resp_detalhe_modulo.status_code == 200


def test_titulo_modulo(resp_detalhe_modulo, modulo):
    """
    Certifica de que o título do módulo está presente na página de detalhes deste.
    """
    assert_contains(resp_detalhe_modulo, modulo.titulo)


def test_descricao_modulo(resp_detalhe_modulo, modulo):
    """
    Certifica de que a descrição do módulo está presente na página de detalhes deste.
    """
    assert_contains(resp_detalhe_modulo, modulo.descricao)


def test_publico_modulo(resp_detalhe_modulo, modulo):
    """
    Certifica de que o público do módulo está presente na página de detalhes deste.
    """
    assert_contains(resp_detalhe_modulo, modulo.publico)


def test_titulo_aulas_modulo(resp_detalhe_modulo, modulo):
    """
    Certifica de os títulos de todas as aulas vinculadas ao módulo estão presentes na página de detalhes deste.
    """
    for aula in modulo.aula_set.all():
        assert_contains(resp_detalhe_modulo, aula.titulo)


def test_link_aulas_modulo(resp_detalhe_modulo, modulo):
    """
    Certifica de que os links que direcionam para a página de detalhes da aula estão presentes, para cada aula, na
    página de detalhes do módulo.
    """
    for aula in modulo.aula_set.all():
        assert_contains(resp_detalhe_modulo, reverse(
            'modulos:detalhe_aula', kwargs={'modulo_slug': modulo.slug, 'slug': aula.slug}))


def test_modulo_sem_aulas(resp_detalhe_modulo_sem_aulas, modulo_sem_aulas):
    """
    Certifica de que, ao acessar a página de detalhes de um módulo sem aulas vinculadas a mensagem "Não há aulas
    cadastradas" é exibida para o usuário.
    :param resp_modulo_sem_aulas: Resposta da requisição para a página de um módulo sem aulas vinculadas.
    """
    assert_contains(resp_detalhe_modulo_sem_aulas, '<li>Não há aulas cadastradas.</li>')


def test_titulo_modulo_breadcrumb(resp_detalhe_modulo, modulo):
    """
    Certifica de que o título do módulo está presente no breadcrumb.
    """
    assert_contains(resp_detalhe_modulo, f'<li class="breadcrumb-item active" aria-current="page">{modulo.titulo}</li>')


def test_indice_modulos_breadcrumb(resp_detalhe_modulo, modulo):
    """
    Certifica de que o índice dos módulos está presente no breadcrumb.
    """
    assert_contains(resp_detalhe_modulo, f'<li class="breadcrumb-item"><a class="text-decoration-none" '
                                         f'href="{reverse("modulos:indice_modulos")}">Módulos</a></li>')


def test_link_home_breadcrumb(resp_detalhe_modulo, modulo):
    """
    Certifica de que o link para a home page está presente no breadcrumb.
    """
    assert_contains(resp_detalhe_modulo, f'<li class="breadcrumb-item"><a '
                                         f'class="text-decoration-none" href="{reverse("base:home")}">Home</a></li>')
