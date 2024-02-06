import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    response = client.get(reverse('base:user_creation'))
    return response


def test_status_code_user_creation_page(resp):
    assert resp.status_code == 200
