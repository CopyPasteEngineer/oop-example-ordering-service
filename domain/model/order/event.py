from domain.model.base.event import DomainEvent
from domain.model.maps import Address
from domain.model.product import PriceThb
from domain.model.payment import PaymentId

from .order_id import OrderId
from .buyer_id import BuyerId
from .line import OrderLineList


class OrderCreated(DomainEvent):
    def __init__(self, order_id: OrderId, buyer_id: BuyerId, lines: OrderLineList,
                 product_cost: PriceThb, delivery_cost: PriceThb, payment_id: PaymentId, destination: Address):
        self._order_id: OrderId = OrderId(order_id)
        self._buyer_id: BuyerId = BuyerId(buyer_id)
        self._lines: OrderLineList = OrderLineList(lines)
        self._product_cost: PriceThb = PriceThb(product_cost)
        self._delivery_cost: PriceThb = PriceThb(delivery_cost)
        self._payment_id: PaymentId = PaymentId(payment_id)
        self._destination: Address = destination

    def serialize(self):
        return {
            'order_id':  self._order_id.serialize(),
            'buyer_id':  self._buyer_id.serialize(),
            'lines':  self._lines.serialize(),
            'product_cost':  self._product_cost.serialize(),
            'delivery_cost':  self._delivery_cost.serialize(),
            'payment_id':  self._payment_id.serialize(),
            'destination':  self._destination.serialize(),
        }


class OrderPaid(DomainEvent):
    def __init__(self, order_id: OrderId, buyer_id: BuyerId, lines: OrderLineList,
                 product_cost: PriceThb, delivery_cost: PriceThb, payment_id: PaymentId):
        self._order_id: OrderId = OrderId(order_id)
        self._buyer_id: BuyerId = BuyerId(buyer_id)
        self._lines: OrderLineList = OrderLineList(lines)
        self._product_cost: PriceThb = PriceThb(product_cost)
        self._delivery_cost: PriceThb = PriceThb(delivery_cost)
        self._payment_id: PaymentId = PaymentId(payment_id)

    def serialize(self):
        return {
            'order_id':  self._order_id.serialize(),
            'buyer_id':  self._buyer_id.serialize(),
            'lines':  self._lines.serialize(),
            'product_cost':  self._product_cost.serialize(),
            'delivery_cost':  self._delivery_cost.serialize(),
            'payment_id':  self._payment_id.serialize(),
        }


class OrderCancelled(DomainEvent):
    def __init__(self, order_id: OrderId, buyer_id: BuyerId, lines: OrderLineList,
                 product_cost: PriceThb, delivery_cost: PriceThb, payment_id: PaymentId):
        self._order_id: OrderId = OrderId(order_id)
        self._buyer_id: BuyerId = BuyerId(buyer_id)
        self._lines: OrderLineList = OrderLineList(lines)
        self._product_cost: PriceThb = PriceThb(product_cost)
        self._delivery_cost: PriceThb = PriceThb(delivery_cost)
        self._payment_id: PaymentId = PaymentId(payment_id)

    def serialize(self):
        return {
            'order_id':  self._order_id.serialize(),
            'buyer_id':  self._buyer_id.serialize(),
            'lines':  self._lines.serialize(),
            'product_cost':  self._product_cost.serialize(),
            'delivery_cost':  self._delivery_cost.serialize(),
            'payment_id':  self._payment_id.serialize(),
        }
