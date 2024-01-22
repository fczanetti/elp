import pytest
from model_bakery import baker
from django.contrib.auth import get_user_model


@pytest.fixture
def usuario_senha_plana(db):
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
def client_usuario_logado(usuario_senha_plana, client):
    """
    Cria um client logado na plataforma para fazer requisições onde o login é necessário.
    :param usuario_senha_plana: Usuário utilizado para login.
    :return: Client logado na plataforma.
    """
    client.force_login(usuario_senha_plana)
    return client
