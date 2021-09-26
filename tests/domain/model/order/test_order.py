import pytest
from domain.model.order import Order, OrderId, BuyerId, OrderLineList, OrderStatus, OrderLine, OrderAmount
from domain.model.order.event import OrderPaid, OrderCancelled
from domain.model.product import PriceThb, ProductId
from domain.model.payment import PaymentId

from domain.model.registry import DomainRegistry
from domain.model.base.event import DummyEventPublisher


@pytest.fixture
def event_publisher():
    return DummyEventPublisher()


@pytest.fixture
def domain_registry():
    registry = DomainRegistry()
    registry.reset()
    registry.assign_defaults()
    return registry


def build_dummy_order(status='waiting'):
    order_id = OrderId('ooo')
    buyer_id = BuyerId('bbb')
    lines = OrderLineList([OrderLine(ProductId('ppp1'), OrderAmount(2)), OrderLine(ProductId('ppp2'), OrderAmount(8))])
    product_cost = PriceThb(123.1)
    delivery_cost = PriceThb(456.2)
    payment_id = PaymentId('qqq')
    status = OrderStatus(status)
    version = 2
    order = Order(order_id=order_id, buyer_id=buyer_id, lines=lines, product_cost=product_cost,
                  delivery_cost=delivery_cost,
                  payment_id=payment_id, status=status, version=version)

    return order


def build_dummy_data(status='waiting'):
    return {
        'order_id': 'ooo',
        'buyer_id': 'bbb',
        'lines': [
            {'product_id': 'ppp1', 'amount': 2},
            {'product_id': 'ppp2', 'amount': 8},
        ],
        'product_cost': 123.1,
        'delivery_cost': 456.2,
        'payment_id': 'qqq',
        'status': status,
        'version': 2,
    }


def test_serialize():
    original = build_dummy_order()
    result = original.serialize()
    expected = build_dummy_data()
    assert result == expected


def test_deserialize():
    raw = build_dummy_data()
    expected = build_dummy_order()
    result = Order.deserialize(raw)
    assert all([
        result.order_id == expected.order_id,
        result.buyer_id == expected.buyer_id,
        result.lines == expected.lines,
        result.product_cost == expected.product_cost,
        result.delivery_cost == expected.delivery_cost,
        result.payment_id == expected.payment_id,
        result._status == expected._status,
        result.version == expected.version,
    ])


def test_is_waiting():
    order = build_dummy_order(status='waiting')
    assert order.is_waiting()


def test_is_cancelled():
    order = build_dummy_order(status='cancelled')
    assert order.is_cancelled()


def test_is_paid():
    order = build_dummy_order(status='paid')
    assert order.is_paid()


def test_pay_when_waiting(domain_registry, event_publisher):
    domain_registry.event_publisher = event_publisher

    order = build_dummy_order(status='waiting')

    order.pay()
    assert order.is_paid()

    assert len(event_publisher.events) == 1 and isinstance(event_publisher.events[0], OrderPaid)  # TODO: test fields
