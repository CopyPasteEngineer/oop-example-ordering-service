import pytest
from domain.model.order import OrderStatus


def test_status_string():
    OrderStatus('waiting')
    OrderStatus('cancelled')
    OrderStatus('paid')


def test_status_enum():
    OrderStatus(OrderStatus.Enum.WAITING)
    OrderStatus(OrderStatus.Enum.CANCELLED)
    OrderStatus(OrderStatus.Enum.PAID)


def test_status_status():
    original = OrderStatus('waiting')
    new = OrderStatus(original)
    assert original == new


def test_status_wrong_type():
    with pytest.raises(TypeError):
        OrderStatus(1234)


def test_province_typo():
    with pytest.raises(ValueError):
        OrderStatus('TYPO')


def test_is_waiting():
    assert OrderStatus('waiting').is_waiting()
    assert not OrderStatus('cancelled').is_waiting()
    assert not OrderStatus('paid').is_waiting()


def test_is_cancelled():
    assert OrderStatus('cancelled').is_cancelled()
    assert not OrderStatus('waiting').is_cancelled()
    assert not OrderStatus('paid').is_cancelled()


def test_is_paid():
    assert OrderStatus('paid').is_paid()
    assert not OrderStatus('cancelled').is_paid()
    assert not OrderStatus('waiting').is_paid()
