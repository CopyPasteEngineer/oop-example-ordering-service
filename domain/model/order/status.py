from typing import Union
from enum import Enum

from domain.model.base import PrimitiveValueObject


class OrderStatusEnum(str, Enum):
    WAITING: str = 'waiting'
    PAID: str = 'paid'
    CANCELLED: str = 'cancelled'

    @classmethod
    def has_value(cls, value):
        return value in cls._member_map_.values()


class OrderStatus(PrimitiveValueObject[str]):
    Enum = OrderStatusEnum

    def __init__(self, status: Union[str, 'OrderStatus']) -> object:
        value: str = self._validate(status)
        super().__init__(value)

    def is_waiting(self) -> bool:
        return self._value == OrderStatusEnum.WAITING

    def is_paid(self) -> bool:
        return self._value == OrderStatusEnum.PAID

    def is_cancelled(self) -> bool:
        return self._value == OrderStatusEnum.CANCELLED

    @staticmethod
    def _validate(status):
        if isinstance(status, str):
            if not OrderStatusEnum.has_value(status):
                raise ValueError(f'OrderStatus named "{status}" not exists')
            value = status
        elif isinstance(status, OrderStatusEnum):
            value = status.value
        elif isinstance(status, OrderStatus):
            value = status._value
        else:
            raise TypeError(f'Expect value of type (str, OrderStatus), got {type(status)}')

        return value
