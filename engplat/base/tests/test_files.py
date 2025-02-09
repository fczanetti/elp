from django.urls import reverse

from engplat.django_assertions import assert_contains


def test_files_page_should_be_loaded(client):
    url = reverse("base:files")
    resp = client.get(url)

    assert resp.status_code == 200


def test_title_should_be_present(client):
    url = reverse("base:files")
    resp = client.get(url)

    assert_contains(resp, "<title>Arquivos</title>")


def test_breadcrumb_is_present(client):
    url = reverse("base:files")
    resp = client.get(url)

    assert_contains(resp, '<nav aria-label="breadcrumb" class="bg-secondary-subtle mb-3 p-3">')
    assert_contains(
        resp, f'<li class="breadcrumb-item"><a class="text-decoration-none" href="{reverse("base:home")}">Home</a></li>'
    )
    assert_contains(resp, '<li class="breadcrumb-item active" aria-current="page">Arquivos</li>')
