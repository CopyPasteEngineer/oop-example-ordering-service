import pytest
from domain.model.order import OrderAmount


def test_amount_int():
    OrderAmount(123)
    OrderAmount(0)


def test_amount_int_less_than_0():
    with pytest.raises(ValueError):
        OrderAmount(-1)


def test_amount_float():
    with pytest.raises(TypeError):
        OrderAmount(0.1)
