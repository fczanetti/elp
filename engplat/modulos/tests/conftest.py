import pytest
from model_bakery import baker
from django.urls import reverse


@pytest.fixture
def modulo(db):
    """
    Cria um módulo com parâmetros aleatórios.
    :return: Módulo criado com parâmetros aleatórios.
    """
    return baker.make('Modulo')


@pytest.fixture
def modulos_desordenados(db):
    """
    Esta função cria módulos não ordenados para que sejam ordenados pela função no módulo facade.py.
    :return: lista de módulos não ordenados.
    """
    modulos = [baker.make('Modulo', order=v, titulo='moduloteste09') for v in [2, 0, 3, 1]]
    return modulos


@pytest.fixture
def modulo_sem_aulas(db):
    """
    Cria um módulo sem aulas para teste de mensagem de aulas não cadastradas.
    """
    return baker.make('Modulo')


@pytest.fixture
def aula(modulo):
    """
    Cria uma aula com parâmetros aleatórios relacionada com o módulo informado no parâmetro da função.
    :param modulo: Módulo para o qual a aula será criada.
    :return: Aula criada para o módulo informado no parâmetro.
    """
    return baker.make('Aula', modulo=modulo, descricao='Descrição de aula')


@pytest.fixture
def aulas(modulo):
    """
    Cria aulas de forma desordenada para que sejam ordenadas e comparadas com o resultado da função que busca e ordena.
    :param modulo: Módulo para o qual as aulas serão criadas.
    :return: Lista de aulas desordenada.
    """
    aulas = [baker.make('Aula', modulo=modulo, order=v) for v in [2, 1, 3]]
    return aulas


@pytest.fixture
def resp_indice_modulos(client_usuario_logado, modulos_desordenados):
    """
    Cria uma requisição na página de índice de módulos com USUÁRIO LOGADO onde devem constar os 3 módulos criados.
    :return: resposta da requisição feita.
    """
    return client_usuario_logado.get(reverse('modulos:indice_modulos'))


@pytest.fixture
def resp_indice_modulos_usuario_nao_logado(client, modulos_desordenados):
    """
    Cria uma requisição na página de índice de módulos com USUÁRIO NÃO LOGADO onde devem constar os 3 módulos criados.
    :return: resposta da requisição feita.
    """
    return client.get(reverse('modulos:indice_modulos'))


@pytest.fixture
def resp_detalhe_modulo(client_usuario_logado, modulo, aulas):
    """
    Gera uma requisição com USUÁRIO LOGADO para a página de detalhes do módulo informado nos parâmetros.
    :param modulo: Modulo usado para renderizar a página/gerar a requisição.
    :return: Resposta da requisição gerada.
    """
    return client_usuario_logado.get(reverse('modulos:detalhe_modulo', args=(modulo.slug,)))


@pytest.fixture
def resp_detalhe_modulo_sem_usuario_logado(client, modulo):
    """
    Gera uma requisição com USUÁRIO NÃO LOGADO para a página de detalhes do módulo informado nos parâmetros.
    :param modulo: Modulo usado para renderizar a página/gerar a requisição.
    :return: Resposta da requisição gerada.
    """
    return client.get(reverse('modulos:detalhe_modulo', args=(modulo.slug,)))


@pytest.fixture
def resp_detalhe_modulo_sem_aulas(client_usuario_logado, modulo_sem_aulas):
    """
    Gera uma requisição COM USUÁRIO LOGADO para a página de detalhes do módulo criado sem aulas relacionadas.
    :param modulo_sem_aulas: Modulo usado para gerar a requisição/renderizar a página.
    :return: Resposta da requisição gerada.
    """
    # return client.get(reverse('modulos:detalhe_modulo', args=(modulo_sem_aulas.slug,)))
    return client_usuario_logado.get(modulo_sem_aulas.get_absolute_url())


@pytest.fixture
def resp_detalhe_aula(client_usuario_logado, aula):
    """
    Gera uma requisição COM USUÁRIO LOGADO para a página de detalhes da aula informada nos parâmetros.
    :param aula: Aula usada para renderizar a página ao criar a requisição.
    :return: Resposta da requisição gerada.
    """
    return client_usuario_logado.get(reverse('modulos:detalhe_aula', kwargs={'slug': aula.slug,
                                                                             'modulo_slug': aula.modulo.slug}))


@pytest.fixture
def resp_detalhe_aula_sem_usuario_logado(client, aula):
    """
    Gera uma requisição com USUÁRIO NÃO LOGADO para a página de detalhes da aula informada nos parâmetros.
    :param aula: Aula usada para renderizar a página ao criar a requisição.
    :return: Resposta da requisição gerada.
    """
    return client.get(reverse('modulos:detalhe_aula', kwargs={'slug': aula.slug,
                                                              'modulo_slug': aula.modulo.slug}))
