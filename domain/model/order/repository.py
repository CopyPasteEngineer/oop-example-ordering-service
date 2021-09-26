from typing import Dict
import uuid
from abc import ABC

from domain.model.base.repository import RepositoryAbstract, EntityNotFound, EntityOutdated

from .order_id import OrderId
from .order import Order


class OrderRepositoryAbstract(RepositoryAbstract[OrderId, Order], ABC):
    pass


class DictOrderRepository(OrderRepositoryAbstract):
    def __init__(self):
        self._storage: Dict[OrderId, Order] = {}

    async def next_identity(self) -> OrderId:
        return OrderId(str(uuid.uuid4()))

    async def from_id(self, id_: OrderId) -> Order:
        try:
            return self._storage[id_]
        except KeyError:
            raise EntityNotFound(f'Order with OrderId {str(id_)} not found')

    async def save(self, entity: Order):
        id_ = entity.order_id
        try:
            old = self._storage[id_]
        except KeyError:
            self._storage[id_] = entity
            return

        entity.increase_version()
        if old.version >= entity.version:
            raise EntityOutdated()

        self._storage[id_] = entity
