import pytest
from products import Product


def test_create_product():
    assert Product("Microsoft Windows", 140.5, 200)


def test_creating_product_invalid_details():
    with pytest.raises(ValueError):
        Product("", -120, -100)


def test_product_becomes_inactive():
    gems = Product("Gems", 100.80, 20)
    assert gems.is_active()  # Check if the product is initially active
    gems.buy(20)
    assert not gems.is_active()  # Check if the product becomes inactive


def test_buy_modifies_quantity():
    product = Product("Example Product", 50.0, 100)
    product.buy(20)
    assert product.get_quantity() == 80


def test_buy_too_much():
    product = Product("Example Product", 50.0, 100)
    with pytest.raises(ValueError):
        product.buy(101)


pytest.main()
