from typing import Union

from domain.model.base import PrimitiveValueObject


class DistanceKm(PrimitiveValueObject[float]):
    def __init__(self, distance: Union[float, 'DistanceKm']):
        value: float = self._validate(distance)
        super().__init__(value)

    @staticmethod
    def _validate(distance):
        if isinstance(distance, float):
            value = distance
        elif isinstance(distance, DistanceKm):
            value = distance._value
        else:
            raise TypeError(f'Expect value of type (int, DistanceKm), got {type(distance)}')

        if value < 0:
            raise ValueError(f'Expected DistanceKm >= 0, got {value}')

        return value
