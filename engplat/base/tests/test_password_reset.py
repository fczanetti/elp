from django.urls import reverse


def test_redirect_reset_password(resp_reset_password):
    """
    Certifica de que após a solicitação de reset de password o usuário é redirecionado para a página customizada.
    """
    assert resp_reset_password.status_code == 302
    assert resp_reset_password.url == reverse('base:password_reset_confirmed')
