from typing import TYPE_CHECKING

from domain.model.base.event import DomainEvent
from domain.model.base.model import Attribute
from domain.model.maps import Address
from domain.model.product import PriceThb
from domain.model.payment import PaymentId

from .order_id import OrderId
from .buyer_id import BuyerId
from .line import OrderLineList


class OrderCreated(DomainEvent):
    order_id: OrderId = Attribute()
    buyer_id: BuyerId = Attribute()
    lines: OrderLineList = Attribute()
    product_cost: PriceThb = Attribute()
    delivery_cost: PriceThb = Attribute()
    payment_id: PaymentId = Attribute()
    destination: Address = Attribute()

    if TYPE_CHECKING:
        def __init__(self, order_id: OrderId, buyer_id: BuyerId, lines: OrderLineList,
                     product_cost: PriceThb, delivery_cost: PriceThb, payment_id: PaymentId, destination: Address):
            super().__init__()


class OrderPaid(DomainEvent):
    order_id: OrderId = Attribute()
    buyer_id: BuyerId = Attribute()
    lines: OrderLineList = Attribute()
    product_cost: PriceThb = Attribute()
    delivery_cost: PriceThb = Attribute()
    payment_id: PaymentId = Attribute()

    if TYPE_CHECKING:
        def __init__(self, *, order_id: OrderId, buyer_id: BuyerId, lines: OrderLineList,
                     product_cost: PriceThb, delivery_cost: PriceThb, payment_id: PaymentId):
            super().__init__()


class OrderCancelled(DomainEvent):
    order_id: OrderId = Attribute()
    buyer_id: BuyerId = Attribute()
    lines: OrderLineList = Attribute()
    product_cost: PriceThb = Attribute()
    delivery_cost: PriceThb = Attribute()
    payment_id: PaymentId = Attribute()

    if TYPE_CHECKING:
        def __init__(self, *, order_id: OrderId, buyer_id: BuyerId, lines: OrderLineList,
                     product_cost: PriceThb, delivery_cost: PriceThb, payment_id: PaymentId):
            super().__init__()
