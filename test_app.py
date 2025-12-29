import pytest
from products import Product
from store import Store


def test_order_too_large():
    """Test that buying more than available quantity raises ValueError."""
    product = Product("Test Product", price=10, quantity=5)
    with pytest.raises(ValueError, match="Not enough quantity."):
        product.buy(10)


def test_product_out_of_stock():
    """Test that product becomes inactive when quantity reaches zero."""
    product = Product("Test Product", price=10, quantity=3)
    product.buy(3)
    assert product.get_quantity() == 0
    assert not product.is_active()


def test_invalid_quantity():
    """Test that setting negative quantity raises ValueError."""
    product = Product("Test Product", price=10, quantity=5)
    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        product.set_quantity(-3)


def test_store_order():
    """Test that store order calculates total price correctly."""
    p1 = Product("Item 1", price=10, quantity=10)
    p2 = Product("Item 2", price=5, quantity=20)
    store = Store([p1, p2])

    total = store.order([(p1, 2), (p2, 4)])
    assert total == 10*2 + 5*4
    assert p1.get_quantity() == 8
    assert p2.get_quantity() == 16


def test_inactive_products_hidden():
    """Test that inactive products are not returned by get_all_products."""
    product = Product("Hidden Item", price=10, quantity=1)
    store = Store([product])

    product.buy(1)
    assert product not in store.get_all_products()