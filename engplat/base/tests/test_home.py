import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    resposta = client.get(reverse('base:home'))
    return resposta


def test_status_code_home(resp):
    assert resp.status_code == 200
