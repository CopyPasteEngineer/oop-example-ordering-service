from typing import List
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError

from domain.model.base import EntityOutdated
from domain.model.order import OrderRepositoryAbstract, Order, OrderId


class MongoDBOrderRepository(OrderRepositoryAbstract):
    def __init__(self, mongo_db, collection_name='order'):
        self.db = mongo_db
        self.collection_name = collection_name

    async def next_identity(self) -> OrderId:
        return OrderId(str(ObjectId()))

    async def all(self, limit=10) -> List[Order]:
        raw_list = await self.db[self.collection_name].find().to_list(limit)
        return [Order.deserialize(raw) for raw in raw_list]

    async def from_id(self, id_: OrderId) -> Order:
        raw = await self.db[self.collection_name].find_one({'_id': ObjectId(str(id_))})
        return Order.deserialize(raw)

    async def save(self, entity: Order):
        data = entity.serialize()
        id_ = ObjectId(str(entity.order_id))

        spec = {'_id': id_, 'version': entity.version}
        update = {'$set': data, '$inc': {'version': 1}}
        del data['version']

        try:
            await self.db[self.collection_name].update_one(spec, update, upsert=True)
        except DuplicateKeyError:
            raise EntityOutdated()
