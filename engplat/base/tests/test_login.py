from django.urls import reverse
from engplat.django_assertions import assert_contains


def test_status_code_pagina_login(resp_login_page):
    """
    Checa se a requisição foi retornada com sucesso.
    """
    assert resp_login_page.status_code == 200


def test_campos_formulario_pagina_login(resp_login_page):
    """
    Certifica de que os campos do formulário de login estão presentes na página.
    """
    assert_contains(resp_login_page, '<label for="id_username">Endereço de email:</label>')
    assert_contains(resp_login_page, '<input type="text" name="username"')
    assert_contains(resp_login_page, '<label for="id_password">Senha:</label>')
    assert_contains(resp_login_page, '<input type="password" name="password"')
    assert_contains(resp_login_page, '<input type="submit" value="Login" class="align-self-end formbutton">')


def test_login_redirect(resp_login_redirect):
    """
    Certifica de que, ao realizar login, a página é redirecionada (status_code 302) para a home page (url base:home).
    """
    assert resp_login_redirect.status_code == 302
    assert resp_login_redirect.url == reverse('base:home')


def test_link_pagina_reset_password(resp_login_page):
    """
    Certifica de que o link da página de recuperação de senha está disponível na página de login.
    """
    assert_contains(resp_login_page, f'<p><a href="{reverse("base:password_reset")}" '
                                     f'class="btn lh-sm bg-body-secondary border">Esqueceu sua senha?</a></p>')


def test_botao_login(resp_login_page):
    """
    Certifica de que, caso o usuário não esteja logado, existe um botão para login na página.
    """
    assert_contains(resp_login_page, f'<a href="{reverse("base:login")}" type="button" '
                                     f'class="btn btn-light m-2">Login</a>')


def test_botao_logout(resp_usuario_logado, usuario_senha_plana):
    """
    Certifica de que, com o usuário logado, o botão de logout aparece na página.
    """
    assert_contains(resp_usuario_logado, '<button class="btn btn-danger m-2" type="submit">Logout</button>')
    assert_contains(resp_usuario_logado, f'{reverse("base:logout")}')
    assert_contains(resp_usuario_logado, f'{usuario_senha_plana.first_name}')
