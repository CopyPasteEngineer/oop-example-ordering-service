from typing import Union, TYPE_CHECKING
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
    value_type = str
    Enum = OrderStatusEnum

    def is_waiting(self) -> bool:
        return self._value == OrderStatusEnum.WAITING

    def is_paid(self) -> bool:
        return self._value == OrderStatusEnum.PAID

    def is_cancelled(self) -> bool:
        return self._value == OrderStatusEnum.CANCELLED

    @classmethod
    def _validate(cls, status):
        if isinstance(status, OrderStatusEnum):
            status = status.value
        value = super()._validate(status)

        if not OrderStatusEnum.has_value(value):
            raise ValueError(f'OrderStatus named "{value}" not exists')

        return value

    if TYPE_CHECKING:
        def __init__(self, status: Union[str, 'OrderStatus']):
            super().__init__(...)
