import pytest
from model_bakery import baker

from engplat.podcasts import facade


@pytest.fixture
def podcasts(db):
    return [baker.make('Podcast', data_gravacao=d) for d in ['2024-01-10', '2024-01-12']]


def test_listar_podcasts_ordenados(podcasts):
    assert list(sorted(podcasts, key=lambda pod: pod.data_gravacao, reverse=True)) == facade.buscar_podcasts_ordenados()
