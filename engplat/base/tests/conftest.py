import pytest
from django.urls import reverse


@pytest.fixture
def resp_login_page(client):
    """
    Gera uma requisição na página de login do usuário.
    :return: Resposta da requisição gerada.
    """
    return client.get(reverse('base:login'))


@pytest.fixture
def resp_usuario_logado(client_usuario_logado):
    """
    Realiza uma requisição na home page com o usuário logado na plataforma.
    :return: Resposta da requisição gerada.
    """
    return client_usuario_logado.get(reverse('base:home'))


@pytest.fixture
def resp_login_redirect(usuario_senha_plana, client):
    """
    Realiza login com os dados do usuário criado.
    :return: Resposta da requisição POST para realização do login.
    """
    return client.post(reverse('base:login'), {'username': usuario_senha_plana.get_username(),
                                               'password': usuario_senha_plana.senha_plana})


@pytest.fixture
def resp_reset_password_page(client):
    """
    Gera uma requisição na página de reset de password.
    :return: Resposta da requisição gerada.
    """
    return client.get(reverse('base:password_reset'))


@pytest.fixture
def resp_password_change_page(client, resp_login_redirect):
    """
    Gera uma requisição na página de alteração de password. Para que a página de alteração de password seja acessada
    é necessário um usuário logado, por isso a necessidade de se utilizar a fixture resp_login_redirect.
    """
    return client.get(reverse('base:password_change'))


@pytest.fixture
def resp_password_change_redirect(usuario_senha_plana, resp_login_redirect, client):
    """
    Altera o password do usuario logado.
    :return: Resposta da requisição POST para realização dda alteração do password.
    """
    novasenha = 'Novopass123#'
    return client.post(reverse('base:password_change'), {'old_password': usuario_senha_plana.senha_plana,
                                                         'new_password1': novasenha,
                                                         'new_password2': novasenha})


@pytest.fixture
def resp_reset_password(client, usuario_senha_plana):
    """
    Realiza uma requisição post na página de reset de password.
    """
    return client.post(reverse('base:password_reset'), {'email': usuario_senha_plana.get_username()})
