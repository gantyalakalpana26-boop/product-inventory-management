import pytest

from inventory import (
    apply_discount,
    calculate_total_price,
    check_stock,
)


# Test calculate_total_price()
def test_calculate_total_price():
    assert calculate_total_price(500, 3) == 1500


def test_calculate_total_price_invalid_price():
    with pytest.raises(ValueError):
        calculate_total_price(-100, 2)


# Test apply_discount()
def test_apply_discount():
    assert apply_discount(2000, 10) == 1800


def test_apply_discount_boundary():
    assert apply_discount(1000, 100) == 0


def test_apply_discount_invalid():
    with pytest.raises(ValueError):
        apply_discount(1000, 150)


# Test check_stock()
def test_check_stock_available():
    assert check_stock(100, 50) == "Stock available"


def test_check_stock_unavailable():
    assert check_stock(10, 20) == "Insufficient stock"


def test_check_stock_invalid():
    with pytest.raises(ValueError):
        check_stock(10, 0)
