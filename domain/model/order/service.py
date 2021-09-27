from domain.model.registry import DomainRegistry
from domain.model.base import optimistic_lock

from domain.model.maps import Address

from .order_id import OrderId
from .buyer_id import BuyerId
from .line import OrderLineList
from .order import Order
from .event import OrderCreated


class OrderService:
    def __init__(self):
        self.registry = DomainRegistry()

    async def new_order(self, buyer_id: BuyerId, lines: OrderLineList, destination: Address) -> OrderId:
        product_counts = [(line.product_id, int(line.amount)) for line in lines]
        total_product_cost = await self.registry.product_service.total_price(product_counts)

        payment_id = await self.registry.payment_service.new_payment(total_product_cost)
        delivery_cost = await self.registry.delivery_cost_calculator.calculate_cost(total_product_cost, destination)
        order_id = await self.registry.order_repository.next_identity()

        order = Order(order_id=order_id, buyer_id=buyer_id, lines=lines,
                      product_cost=total_product_cost, delivery_cost=delivery_cost,
                      payment_id=payment_id)
        await self._save_new_order(order)

        event = OrderCreated(order_id=order_id, buyer_id=buyer_id, lines=lines,
                             product_cost=total_product_cost, delivery_cost=delivery_cost,
                             payment_id=payment_id, destination=destination)
        self.registry.event_publisher.publish(event)

        return order.order_id

    @optimistic_lock
    async def _save_new_order(self, order: Order):
        return await self.registry.order_repository.save(order)
