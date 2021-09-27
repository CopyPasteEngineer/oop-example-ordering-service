from typing import Union

from domain.model.base import PrimitiveValueObject


class OrderAmount(PrimitiveValueObject[int]):
    value_type = int

    def __init__(self, amount: Union[int, 'OrderAmount']):
        value: int = self._validate(amount)
        super().__init__(value)

    @classmethod
    def _validate(cls, value):
        value = super()._validate(value)

        if value < 0:
            raise ValueError(f'Expected OrderAmount >= 0, got {value}')

        return value
