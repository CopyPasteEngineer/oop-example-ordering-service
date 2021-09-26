from typing import Union, TypeVar, Generic

from .primitive_value_object import PrimitiveValueObject


ImplementationType = TypeVar('ImplementationType', bound='StrIdValueObject')


class StrIdValueObject(PrimitiveValueObject[str], Generic[ImplementationType]):
    def __init__(self, id_: Union[str, ImplementationType]):
        value: str = self._validate(id_)
        super().__init__(value)

    @classmethod
    def _validate(cls, id_):
        if isinstance(id_, str):
            value = id_
        elif isinstance(id_, cls):
            value = id_._value
        else:
            raise TypeError(f'Expect value of type (str, {cls.__name__}), got {type(id_)}')

        return value

    def __str__(self):
        return self._value
