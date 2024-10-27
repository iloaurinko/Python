from shopping_cart import Item

import pytest
#

@pytest.mark.slow
def test_get_all_items(cart):

    milk = Item("Milk", 2)
    apple = Item("Apple", 1)

    cart.add_item(milk)
    cart.add_item(apple)

    assert cart.get_items() == ["Milk", "Apple"]


@pytest.mark.slow
@pytest.mark.windows
def test_get_sum(cart):

    milk = Item("Milk", 2)
    apple = Item("Apple", 1)

    cart.add_item(milk)
    cart.add_item(apple)
    cart.add_item(apple)

    assert cart.get_total() == 4


@pytest.mark.xfail
def test_remove_item(cart):

    milk = Item("Milk", 2)
    apple = Item("Apple", 1)

    cart.add_item(milk)
    cart.add_item(apple)
    cart.remove_item("Apple")

    assert cart.get_items() == ["Milk"]
