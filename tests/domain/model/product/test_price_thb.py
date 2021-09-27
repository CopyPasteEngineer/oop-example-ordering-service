import pytest
from domain.model.product import PriceThb


def test_price_float():
    PriceThb(123.4)
    PriceThb(0.0)


def test_price_float_less_than_0():
    with pytest.raises(ValueError):
        PriceThb(-1.0)


def test_price_int():
    with pytest.raises(TypeError):
        PriceThb(123)
