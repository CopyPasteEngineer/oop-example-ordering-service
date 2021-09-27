from domain.model.base import optimistic_lock
from domain.model.order import BuyerId, OrderLineList, OrderId, Order
from domain.model.maps import Address
from domain.model.registry import DomainRegistry


async def create_new_order(buyer_id: BuyerId, lines: OrderLineList, destination: Address) -> OrderId:
    order_id = await DomainRegistry().order_service.new_order(buyer_id=buyer_id, lines=lines, destination=destination)
    return order_id


@optimistic_lock
async def pay_order(order_id: OrderId):
    repo = DomainRegistry().order_repository

    order = await repo.from_id(order_id)
    order.pay()
    await repo.save(order)


@optimistic_lock
async def cancel_order(order_id: OrderId):
    repo = DomainRegistry().order_repository

    order = await repo.from_id(order_id)
    order.cancel()
    await repo.save(order)


async def get_order_from_id(order_id: OrderId) -> Order:
    order = await DomainRegistry().order_repository.from_id(order_id)
    return order
