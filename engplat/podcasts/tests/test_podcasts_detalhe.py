import pytest
from django.urls import reverse
from model_bakery import baker
from engplat.django_assertions import assert_contains
from engplat.podcasts.models import Podcast


@pytest.fixture
def podcast(db):
    pod = baker.make(Podcast)
    return pod


@pytest.fixture
def resp(client, podcast):
    return client.get(reverse('podcasts:detalhe', args=(podcast.slug,)))


@pytest.fixture
def resp_video_inexistente(client, podcast):
    return client.get(reverse('podcasts:detalhe', args=(podcast.slug+'video_nao_existente',)))


def test_video_inexistente(resp_video_inexistente):
    assert resp_video_inexistente.status_code == 404


def test_status_code_detalhe_podcast(resp):
    assert resp.status_code == 200


def test_titulo_podcast(resp, podcast):
    assert_contains(resp, f'{podcast.titulo}')


def test_video_url_podcast_detalhe(resp, podcast):
    assert_contains(resp, f'https://www.youtube.com/embed/{podcast.plat_id}')


def test_descricao_podcast(resp, podcast):
    assert_contains(resp, f'{podcast.descricao}')
