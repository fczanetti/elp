from django.urls import reverse

from engplat.django_assertions import assert_contains
from engplat.base.models import File

from model_bakery import baker


def test_files_page_should_be_loaded(client_usuario_logado):
    url = reverse("base:files")
    resp = client_usuario_logado.get(url)

    assert resp.status_code == 200


def test_title_should_be_present(client_usuario_logado):
    url = reverse("base:files")
    resp = client_usuario_logado.get(url)

    assert_contains(resp, "<title>Arquivos</title>")


def test_breadcrumb_is_present(client_usuario_logado):
    url = reverse("base:files")
    resp = client_usuario_logado.get(url)

    assert_contains(resp, '<nav aria-label="breadcrumb" class="bg-secondary-subtle mb-3 p-3">')
    assert_contains(
        resp, f'<li class="breadcrumb-item"><a class="text-decoration-none" href="{reverse("base:home")}">Home</a></li>'
    )
    assert_contains(resp, '<li class="breadcrumb-item active" aria-current="page">Arquivos</li>')


def test_should_show_files_to_download(client_usuario_logado, db):
    file_1 = baker.make(File)
    file_2 = baker.make(File)

    url = reverse("base:files")

    resp = client_usuario_logado.get(url)

    assert file_1.title in resp.content.decode()
    assert file_2.title in resp.content.decode()

    assert file_1.file_url in resp.content.decode()
    assert file_2.file_url in resp.content.decode()
