import pytest
from django.urls import reverse

from engplat.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resposta = client.get(reverse('base:home'))
    return resposta


def test_status_code_home(resp):
    assert resp.status_code == 200


def test_link_home_navbar(resp):
    assert_contains(resp, f'href="{reverse("base:home")}"')
