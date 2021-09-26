from typing import Union

from domain.model.base import PrimitiveValueObject


class PriceThb(PrimitiveValueObject[float]):
    def __init__(self, price: Union[float, 'PriceThb']):
        value: float = self._validate(price)
        super().__init__(value)

    @staticmethod
    def _validate(price):
        if isinstance(price, float):
            value = price
        elif isinstance(price, PriceThb):
            value = price._value
        else:
            raise TypeError(f'Expect value of type (float, PriceTHB), got {type(price)}')

        if value < 0:
            raise ValueError(f'Expected PriceTHB >= 0, got {value}')

        return value

    def __float__(self):
        return float(self._value)
