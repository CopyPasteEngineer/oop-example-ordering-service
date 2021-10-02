from typing import List, Tuple

import pytest

from domain.model import DomainRegistry
from domain.model.base.event import DummyEventPublisher

from domain.model.product import ProductServiceAbstract, ProductId, PriceThb
from domain.model.payment import PaymentServiceAbstract, PaymentId
from domain.model.delivery import DeliveryCostCalculator
from domain.model.maps import Address
from domain.model.order import OrderService, DictOrderRepository, BuyerId, OrderLineList, OrderId


@pytest.fixture
def registry():
    reg = DomainRegistry()
    reg.reset()
    reg.event_publisher = DummyEventPublisher()
    return reg


@pytest.fixture
def address_random():
    address = Address.build('123/4', 'ROAD', 'SUBDISTRICT', 'DISTRICT', 'bangkok', '12345', 'THAILAND')
    return address


class MyDummyOrderRepository(DictOrderRepository):
    def __init__(self, next_identity):
        super().__init__()

        self._next_identity = next_identity

    async def next_identity(self) -> OrderId:
        return self._next_identity


class DummyProductService(ProductServiceAbstract):
    def __init__(self, total_price):
        self._total_price = total_price

    async def total_price(self, product_counts: List[Tuple[ProductId, int]]) -> PriceThb:
        return self._total_price


class DummyPaymentService(PaymentServiceAbstract):
    def __init__(self, new_payment):
        self._new_payment = new_payment

    async def new_payment(self, total_price: PriceThb) -> PaymentId:
        return self._new_payment

    async def verify_payment(self, payment_id: PaymentId) -> bool:
        return False


class DummyDeliveryCostCalculator(DeliveryCostCalculator):
    def __init__(self, delivery_cost):
        self._delivery_cost = delivery_cost

    async def calculate_cost(self, total_product_cost: PriceThb, destination: Address) -> PriceThb:
        return self._delivery_cost


@pytest.mark.asyncio
async def test_new_order(registry, address_random):
    registry.order_repository = MyDummyOrderRepository(next_identity=OrderId('ooo'))

    registry.product_service = DummyProductService(total_price=PriceThb(123.4))
    registry.payment_service = DummyPaymentService(new_payment=PaymentId('ppp'))
    registry.delivery_cost_calculator = DummyDeliveryCostCalculator(delivery_cost=567.8)

    # test target
    service = OrderService()
    order_id = await service.new_order(BuyerId('bbb'), lines=OrderLineList([]), destination=address_random)

    expected_order_id = OrderId('ooo')
    assert order_id == expected_order_id

    order = await registry.order_repository.from_id(expected_order_id)
    assert all([
        order.order_id == expected_order_id,
        order.buyer_id == BuyerId('bbb'),
        order.lines == OrderLineList([]),
        order.product_cost == PriceThb(123.4),
        order.delivery_cost == PriceThb(567.8),
        order.payment_id == PaymentId('ppp'),
        order.version == 0,

        order.total_cost == PriceThb(123.4 + 567.8),
    ])
