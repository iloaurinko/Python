import pytest

from shopping_cart import ShoppingCart


@pytest.fixture()
def cart():
    cart = ShoppingCart()

    # print("Подготовка к тесту...")

    yield cart

    # print("После теста...")

    cart.clear()