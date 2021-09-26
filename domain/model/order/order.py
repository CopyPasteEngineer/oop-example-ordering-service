from typing import Dict

from domain.model.registry import DomainRegistry
from domain.model.base import Entity

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


class Order(Entity):
    def __init__(self, order_id: OrderId, buyer_id: BuyerId, lines: OrderLineList,
                 product_cost: PriceThb, delivery_cost: PriceThb, payment_id: PaymentId, *,
                 status: OrderStatus = OrderStatus.Enum.WAITING, version: int = 0):
        self._order_id: OrderId = OrderId(order_id)
        self._buyer_id: BuyerId = BuyerId(buyer_id)
        self._lines: OrderLineList = OrderLineList(lines)
        self._product_cost: PriceThb = PriceThb(product_cost)
        self._delivery_cost: PriceThb = PriceThb(delivery_cost)
        self._payment_id: PaymentId = PaymentId(payment_id)
        self._status: OrderStatus = OrderStatus(status)
        self._version: int = version

    def pay(self):
        if self.is_cancelled():
            raise OrderAlreadyCancelledException('Order\'s already cancelled')
        if self.is_paid():
            raise OrderAlreadyPaidException('Order\'s already paid')

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
    def order_id(self) -> OrderId:
        return self._order_id

    @property
    def buyer_id(self) -> BuyerId:
        return self._buyer_id

    @property
    def lines(self) -> OrderLineList:
        return self._lines

    @property
    def product_cost(self) -> PriceThb:
        return self._product_cost

    @property
    def delivery_cost(self) -> PriceThb:
        return self._delivery_cost

    @property
    def total_cost(self) -> PriceThb:
        return PriceThb(self._product_cost + self._delivery_cost)

    @property
    def payment_id(self) -> PaymentId:
        return self._payment_id

    @property
    def version(self) -> int:
        return self._version

    def increase_version(self):
        self._version += 1

    def serialize(self) -> Dict:
        return {
            'order_id': self._order_id.serialize(),
            'buyer_id': self._buyer_id.serialize(),
            'lines': self._lines.serialize(),
            'product_cost': self._product_cost.serialize(),
            'delivery_cost': self._delivery_cost.serialize(),
            'payment_id': self._payment_id.serialize(),
            'status': self._status.serialize(),
            'version': self._version,
        }

    @classmethod
    def deserialize(cls, value: Dict) -> 'Order':
        order_id = OrderId.deserialize(value.get('order_id'))
        buyer_id = BuyerId.deserialize(value.get('buyer_id'))
        lines = OrderLineList.deserialize(value.get('lines'))
        product_cost = PriceThb.deserialize(value.get('product_cost'))
        delivery_cost = PriceThb.deserialize(value.get('delivery_cost'))
        payment_id = PaymentId.deserialize(value.get('payment_id'))
        status = OrderStatus.deserialize(value.get('status'))
        version = value.get('version', 0)

        return cls(order_id=order_id, buyer_id=buyer_id, lines=lines,
                   product_cost=product_cost, delivery_cost=delivery_cost, payment_id=payment_id,
                   status=status, version=version)
