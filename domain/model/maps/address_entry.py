from typing import Union

from domain.model.base import PrimitiveValueObject


class AddressEntry(PrimitiveValueObject[str]):
    def __init__(self, entry: Union[str, 'AddressEntry']):
        value: str = self._validate(entry)
        super().__init__(value)

    @staticmethod
    def _validate(entry):
        if isinstance(entry, str):
            value = entry
        elif isinstance(entry, AddressEntry):
            value = entry._value
        else:
            raise TypeError(f'Expect value of type (str, AddressEntry), got {type(entry)}')

        return value

    def __str__(self):
        return self._value
