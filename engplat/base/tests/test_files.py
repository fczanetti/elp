from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from engplat.django_assertions import assert_contains
from engplat.base.models import File


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


def test_should_upload_files(client, settings, db):
    settings.STORAGES = {
        "default": {"BACKEND": "django.core.files.storage.InMemoryStorage", },
        "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage", },
    }
    file = SimpleUploadedFile("file.pdf", b"dados", content_type="application/pdf")

    data = {"title": "Título do arquivo", "file": file}
    url = reverse("base:files")

    assert File.objects.exists() is False

    resp = client.post(url, data=data)

    assert File.objects.exists() is True
    file = File.objects.first()

    assert file.title == "Título do arquivo"
    assert "Arquivo salvo com sucesso." in resp.content.decode()


def test_should_show_errors_if_form_is_not_valid(client, settings, db):
    settings.STORAGES = {
        "default": {"BACKEND": "django.core.files.storage.InMemoryStorage", },
        "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage", },
    }
    file = SimpleUploadedFile("file.pdf", b"dados", content_type="application/pdf")

    data = {"title": "Título do arquivo", "file": file}
    data["title"] = "T" * 75  # Too long title
    url = reverse("base:files")

    assert File.objects.exists() is False

    resp = client.post(url, data=data)

    assert File.objects.exists() is False
    assert "Verifique os erros e tente novamente." in resp.content.decode()
    assert "Certifique-se de que o valor tenha no máximo 72 caracteres" in resp.content.decode()
