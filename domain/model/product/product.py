from typing import Dict

from domain.model.base import Entity

from .product_id import ProductId
from .price_thb import PriceThb


class Product(Entity):
    def __init__(self, product_id: ProductId, price: PriceThb):
        self._product_id: ProductId = ProductId(product_id)
        self._price: PriceThb = PriceThb(price)

    @property
    def product_id(self) -> ProductId:
        return self._product_id

    @property
    def price(self) -> PriceThb:
        return self._price

    def serialize(self) -> Dict:
        return {
            'product_id': self._product_id.serialize(),
            'price': self._price.serialize(),
        }

    @classmethod
    def deserialize(cls, value: Dict) -> 'Product':
        product_id = ProductId.deserialize(value['product_id'])
        price = PriceThb.deserialize(value['price'])

        return Product(product_id=product_id, price=price)
