import pytest
from django.urls import reverse
# from engplat.django_assertions import assert_contains
from model_bakery import baker
from engplat.podcasts.models import Podcast


@pytest.fixture
def podcast(db):
    pod = baker.make(Podcast)
    return pod


@pytest.fixture
def resp(client, podcast):
    return client.get(reverse('podcasts:detalhe', args=(podcast.slug,)))


def test_status_code_detalhe_podcast(resp):
    assert resp.status_code == 200
