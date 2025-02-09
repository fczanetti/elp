from django.urls import reverse

from engplat.django_assertions import assert_contains


def test_status_code_home(client):
    url = reverse('base:home')
    resp = client.get(url)

    assert resp.status_code == 200


def test_components_are_present(client):
    url = reverse('base:home')
    resp = client.get(url)

    assert_contains(resp, f'href="{reverse("base:home")}"')
    assert_contains(resp, '<h2>Podcasts</h2>')
    assert_contains(resp, 'href="https://www.youtube.com/@adiadi8803"')
    assert_contains(resp, f'href="{reverse("podcasts:indice")}"')
    assert_contains(resp, f'href="{reverse("base:files")}"')
