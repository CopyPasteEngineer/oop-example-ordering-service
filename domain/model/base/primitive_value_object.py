from typing import TypeVar, Generic, Union, Type

from .value_object import ValueObject


PrimitiveType = TypeVar('PrimitiveType', int, str, float, bool, list)

CompatibleType = Union[PrimitiveType, 'PrimitiveValueObject']

PrimitiveValueObjectType = TypeVar('PrimitiveValueObjectType')


class PrimitiveValueObject(ValueObject, Generic[PrimitiveType]):
    def __init__(self, value: PrimitiveType):
        self._value: PrimitiveType = value

    def __eq__(self, other: CompatibleType) -> bool:
        m = other
        if isinstance(other, PrimitiveValueObject):
            m = other._value
        return self._value == m

    def __hash__(self):
        return self._value.__hash__()

    def __le__(self, other: CompatibleType) -> bool:
        m = other
        if isinstance(other, PrimitiveValueObject):
            m = other._value
        return self._value <= m

    def __ge__(self, other: CompatibleType) -> bool:
        m = other
        if isinstance(other, PrimitiveValueObject):
            m = other._value
        return self._value >= m

    def __lt__(self, other: CompatibleType) -> bool:
        m = other
        if isinstance(other, PrimitiveValueObject):
            m = other._value
        return self._value < m

    def __gt__(self, other: CompatibleType) -> bool:
        m = other
        if isinstance(other, PrimitiveValueObject):
            m = other._value
        return self._value > m

    def __add__(self, other: CompatibleType) -> CompatibleType:
        m = other
        if isinstance(other, PrimitiveValueObject):
            m = other._value
        return self._value + m

    def __sub__(self, other: CompatibleType) -> CompatibleType:
        m = other
        if isinstance(other, PrimitiveValueObject):
            m = other._value
        return self._value - m

    def __mul__(self, other: CompatibleType) -> CompatibleType:
        m = other
        if isinstance(other, PrimitiveValueObject):
            m = other._value
        return self._value * m

    def __truediv__(self, other: CompatibleType) -> CompatibleType:
        m = other
        if isinstance(other, PrimitiveValueObject):
            m = other._value
        return self._value / m

    def serialize(self) -> PrimitiveType:
        return self._value

    @classmethod
    def deserialize(cls: Type[PrimitiveValueObjectType], value) -> PrimitiveValueObjectType:
        return cls(value)
