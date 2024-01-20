from engplat.django_assertions import assert_contains


def test_forgotten_password_status_code(resp_reset_password_page):
    """
    Certifica de que a página de reset de password foi carregada com sucesso.
    """
    assert resp_reset_password_page.status_code == 200


def test_campos_formulario_recuperacao_senha(resp_reset_password_page):
    """
    Certifica de que os campos do formulario de recuperação de senha estão presentes.
    """
    assert_contains(resp_reset_password_page, '<label for="id_email">Endereço de email:</label>')
    assert_contains(resp_reset_password_page, '<input type="email" name="email"')
    assert_contains(resp_reset_password_page, '<input type="submit" value="Reinicializar minha senha">')
