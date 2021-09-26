import re
from typing import Union

from domain.model.base import PrimitiveValueObject


class Postcode(PrimitiveValueObject[str]):
    def __init__(self, postcode: Union[str, 'Postcode']):
        value: str = self._validate(postcode)
        super().__init__(value)

    @staticmethod
    def _validate(postcode):
        if isinstance(postcode, str):
            value = postcode
        elif isinstance(postcode, Postcode):
            value = postcode._value
        else:
            raise TypeError(f'Expect value of type (str, Postcode), got {type(postcode)}')

        if not re.match(r'^\d{5}$', value):
            raise ValueError(f'Postcode must be a string of 5 digits, got {value}')

        return value
