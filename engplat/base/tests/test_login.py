import pytest
from django.urls import reverse
from model_bakery import baker
from django.contrib.auth import get_user_model


@pytest.fixture
def usuario(db):
    """
    Cria um usuário e define uma senha acessível para este.
    :return: Usuário de modelo com password = 'senha'.
    """
    user = baker.make(get_user_model())
    senha = 'senha'
    user.set_password(senha)
    user.save()
    user.senha_plana = senha
    return user


@pytest.fixture
def resp_login_redirect(usuario, client):
    """
    Realiza login com os dados do usuário criado.
    :return: Resposta da requisição POST para realização do login.
    """
    return client.post(reverse('base:user_login'), {'username': usuario.get_username(),
                                                    'password': usuario.senha_plana})


@pytest.fixture
def resp(client):
    """
    Gera uma requisição na página de login do usuário.
    :return: Resposta da requisição gerada.
    """
    return client.get(reverse('base:user_login'))


def test_status_code(resp):
    """
    Checa se a requisição foi retornada com sucesso.
    """
    assert resp.status_code == 200


def test_login_redirect(resp_login_redirect):
    """
    Certifica de que, ao realizar login, a página é redirecionada (status_code 302) para a home page (url base:home).
    """
    assert resp_login_redirect.status_code == 302
    assert resp_login_redirect.url == reverse('base:home')
