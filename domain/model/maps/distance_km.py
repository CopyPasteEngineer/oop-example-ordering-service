from typing import Union, TYPE_CHECKING

from domain.model.base import PrimitiveValueObject


class DistanceKm(PrimitiveValueObject[float]):
    value_type = float

    @classmethod
    def _validate(cls, value):
        value = super()._validate(value)

        if value < 0:
            raise ValueError(f'Expected DistanceKm >= 0, got {value}')

        return value

    if TYPE_CHECKING:
        def __init__(self, value: Union[float, 'DistanceKm']):
            super().__init__(value)
