import pytest
from django.urls import reverse

from engplat.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    response = client.get(reverse('base:user_creation'))
    return response


def test_status_code_user_creation_page(resp):
    assert resp.status_code == 200


def test_user_creation_content_form(resp):
    """
    Certifica de que os componentes do formulário de criação de usuário estão presentes.
    """
    assert_contains(resp, '<label for="id_first_name">Primeiro nome:</label>')
    assert_contains(resp, '<input type="text" name="first_name" maxlength="150" required id="id_first_name">')
    assert_contains(resp, '<label for="id_email">Endereço de email:</label>')
    assert_contains(resp, '<input type="email" name="email" maxlength="254" autofocus required id="id_email">')
    assert_contains(resp, '<label for="id_password1">Senha:</label>')
    assert_contains(resp, '<input type="password" name="password1" autocomplete="new-password" aria-describedby="id_password1_helptext" id="id_password1">')
    assert_contains(resp, '<label for="id_password2">Confirmação de senha:</label>')
    assert_contains(resp, '<input type="password" name="password2" autocomplete="new-password" aria-describedby="id_password2_helptext" id="id_password2">')


def test_successfull_user_creation(client, db):
    """
    Certifica de que, ao criar conta com sucesso, o usuário é redirecionado para a página de usuário criado.
    """
    response = client.post(reverse('base:user_creation'), {'first_name': 'Foo', 'email': 'foo@bar.com',
                                                           'password1': 'TestPass123#', 'password2': 'TestPass123#'})
    assert response.status_code == 302
    assert response.url == f'{reverse("base:user_created")}'
