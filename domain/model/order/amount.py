from typing import Union

from domain.model.base import PrimitiveValueObject


class OrderAmount(PrimitiveValueObject[int]):
    def __init__(self, amount: Union[int, 'OrderAmount']):
        value: int = self._validate(amount)
        super().__init__(value)

    @staticmethod
    def _validate(amount):
        if isinstance(amount, int):
            value = amount
        elif isinstance(amount, OrderAmount):
            value = amount._value
        else:
            raise TypeError(f'Expect value of type (int, OrderAmount), got {type(amount)}')

        if value < 0:
            raise ValueError(f'Expected OrderAmount >= 0, got {value}')

        return value

    def __int__(self):
        return int(self._value)
