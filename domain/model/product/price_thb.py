from typing import Union, TYPE_CHECKING

from domain.model.base import PrimitiveValueObject


class PriceThb(PrimitiveValueObject):
    value_type = float

    @classmethod
    def _validate(cls, price):
        price = super()._validate(price)

        if price < 0:
            raise ValueError(f'Expected PriceTHB >= 0, got {price}')

        return price

    if TYPE_CHECKING:
        def __init__(self, price: Union[float, 'PriceThb']):
            super().__init__(...)
