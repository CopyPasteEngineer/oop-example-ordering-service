from typing import TYPE_CHECKING

from domain.model.registry import DomainRegistry
from domain.model.base import Entity
from domain.model.base.model import Attribute, AttributeSetter

from domain.model.product import PriceThb
from domain.model.payment import PaymentId

from .order_id import OrderId
from .buyer_id import BuyerId
from .line import OrderLineList
from .status import OrderStatus
from .event import OrderPaid, OrderCancelled


class OrderAlreadyCancelledException(Exception):
    pass


class OrderAlreadyPaidException(Exception):
    pass


class PaymentNotVerifiedException(Exception):
    pass


class Order(Entity):
    order_id: OrderId = Attribute()
    buyer_id: BuyerId = Attribute()
    lines: OrderLineList = Attribute()
    product_cost: PriceThb = Attribute()
    delivery_cost: PriceThb = Attribute()
    payment_id: PaymentId = Attribute()
    status: OrderStatus = Attribute(default=OrderStatus.Enum.WAITING)
    version: int = Attribute(default=0)

    def pay(self, is_payment_verified: bool):
        if self.is_cancelled():
            raise OrderAlreadyCancelledException('Order\'s already cancelled')
        if self.is_paid():
            raise OrderAlreadyPaidException('Order\'s already paid')
        if not is_payment_verified:
            raise PaymentNotVerifiedException(f'Payment {self.payment_id} must be verified')

        self._status = OrderStatus(OrderStatus.Enum.PAID)

        event = OrderPaid(order_id=self._order_id, buyer_id=self._buyer_id, lines=self._lines,
                          product_cost=self._product_cost, delivery_cost=self._delivery_cost,
                          payment_id=self._payment_id)
        DomainRegistry().event_publisher.publish(event)

    def cancel(self):
        if self.is_cancelled():
            raise OrderAlreadyCancelledException('Order\'s already cancelled')
        if self.is_paid():
            raise OrderAlreadyPaidException('Order\'s already paid')

        self._status = OrderStatus(OrderStatus.Enum.CANCELLED)

        event = OrderCancelled(order_id=self._order_id, buyer_id=self._buyer_id, lines=self._lines,
                               product_cost=self._product_cost, delivery_cost=self._delivery_cost,
                               payment_id=self._payment_id)
        DomainRegistry().event_publisher.publish(event)

    def is_waiting(self) -> bool:
        return self._status.is_waiting()

    def is_paid(self) -> bool:
        return self._status.is_paid()

    def is_cancelled(self) -> bool:
        return self._status.is_cancelled()

    @property
    def total_cost(self) -> PriceThb:
        return PriceThb(self._product_cost + self._delivery_cost)

    def increase_version(self):
        self._version += 1

    if TYPE_CHECKING:
        def __init__(self, *, order_id: OrderId, buyer_id: BuyerId, lines: OrderLineList,
                     product_cost: PriceThb, delivery_cost: PriceThb, payment_id: PaymentId,
                     status: OrderStatus = OrderStatus.Enum.WAITING, version: int = 0):
            super().__init__()

    _order_id: OrderId = AttributeSetter()
    _buyer_id: BuyerId = AttributeSetter()
    _lines: OrderLineList = AttributeSetter()
    _product_cost: PriceThb = AttributeSetter()
    _delivery_cost: PriceThb = AttributeSetter()
    _payment_id: PaymentId = AttributeSetter()
    _status: OrderStatus = AttributeSetter()
    _version: int = AttributeSetter()
