from engplat.django_assertions import assert_contains
from django.urls import reverse


def test_password_change_status_code(resp_password_change_page):
    """
    Certifica de que a página de reset de password foi carregada com sucesso.
    """
    assert resp_password_change_page.status_code == 200


def test_campos_formulario_alteracao_senha(resp_password_change_page):
    """
    Certifica de que os campos a serem preenchidos para alteração de senha estão presentes.
    """
    assert_contains(resp_password_change_page, '<label for="id_old_password">Senha antiga:</label>')
    assert_contains(resp_password_change_page, '<input type="password" name="old_password"')
    assert_contains(resp_password_change_page, '<label for="id_new_password1">Nova senha:</label>')
    assert_contains(resp_password_change_page, '<input type="password" name="new_password1"')
    assert_contains(resp_password_change_page, '<label for="id_new_password2">Confirmação da nova senha:</label>')
    assert_contains(resp_password_change_page, '<input type="password" name="new_password2"')
    assert_contains(resp_password_change_page, '<input type="submit" value="Alterar minha senha" '
                                               'class="default formbutton align-self-end">')


def test_redirect_after_password_changed_successfuly(resp_password_change_redirect):
    """
    Certifica de que após a alteração do password com sucesso o usuário é redirecionado para a página que informa
    a alteração bem sucedida.
    """
    assert resp_password_change_redirect.status_code == 302
    assert resp_password_change_redirect.url == reverse('base:password_alterado')
