import pytest
from django.urls import reverse
from engplat.django_assertions import assert_contains, assert_not_contains
from model_bakery import baker

from engplat.payments.models import Product


@pytest.fixture
def available_prods(db):
    available_products = baker.make(Product, 3, available=True)
    return available_products


@pytest.fixture
def unavailable_prods(db):
    unavailable_products = baker.make(Product, 3, available=False)
    return unavailable_products


@pytest.fixture
def resp(client, available_prods, unavailable_prods):
    """
    Gera uma requisição na página de produtos.
    """
    response = client.get(reverse('payments:products'))
    return response


def test_status_code_products(resp):
    """
    Certifica de que a página é carregada com sucesso.
    """
    assert resp.status_code == 200


def test_available_products(resp, available_prods):
    """
    Certifica de que os produtos disponíveis estão presentes na página de produtos.
    :param resp:
    :param available_prods:
    :return:
    """
    for prod in available_prods:
        assert_contains(resp, prod.prod_name)
        assert_contains(resp, f'href="{ reverse("payments:product_page", args=(prod.slug,)) }">Adquira já!')
        assert_contains(resp, prod.description)


def test_unavailable_products(resp, unavailable_prods):
    """
    Certifica de que os produtos indisponíveis não aparecem na página de produtos.
    """
    for prod in unavailable_prods:
        assert_not_contains(resp, prod.prod_name)


def test_link_home_breadcrumb(resp):
    """
    Certifica de que o link para a home page está presente no breadcrumb.
    """
    assert_contains(resp, f'<li class="breadcrumb-item"><a class="text-decoration-none" '
                          f'href="{ reverse("base:home") }">Home</a></li>')
