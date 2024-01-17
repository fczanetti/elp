import pytest
from model_bakery import baker
from engplat.podcasts.models import Podcast
from django.urls import reverse


@pytest.fixture
def podcasts_indice(db):
    """
    Cria 3 podcasts com parâmetros aleatórios.
    :return: 3 podcasts.
    """
    pods = baker.make(Podcast, _quantity=3)
    return pods


@pytest.fixture
def podcast_detalhe(db):
    """
    Cria um podcast com parâmetros aleatórios.
    :return: Podcast criado.
    """
    pod = baker.make(Podcast)
    return pod


@pytest.fixture
def resp_indice_podcasts(client, podcasts_indice):
    """
    Gera uma requisição na página de índice de podcasts.
    :param podcasts: Podcasts que deverão aparecer na página.
    :return: Resposta da requisição gerada.
    """
    return client.get(reverse('podcasts:indice'))


@pytest.fixture
def resp_detalhe_podcast(client, podcast_detalhe):
    """
    Gera uma requisição e uma resposta para a página de detalhes do podcast criado.
    :param podcast_detalhe: Podcast que será apresentado na página de detalhes.
    :return: Resposta da requisição criada.
    """
    return client.get(reverse('podcasts:detalhe', args=(podcast_detalhe.slug,)))


@pytest.fixture
def resp_podcast_inexistente(client, podcast_detalhe):
    """
    Certifica de que, ao preencher a URL com um link de podcast que não existe no banco, é retornado o erro 404.
    :return: Resposta apresentando erro 404.
    """
    return client.get(reverse('podcasts:detalhe', args=(podcast_detalhe.slug+'video_nao_existente',)))


@pytest.fixture
def podcasts_datas_especificas(db):
    """
    Cria uma lista com dois podcasts, cada um com uma data de gravação especificada.
    :return: Lista de podcasts.
    """
    return [baker.make('Podcast', data_gravacao=d) for d in ['2024-01-10', '2024-01-12']]
