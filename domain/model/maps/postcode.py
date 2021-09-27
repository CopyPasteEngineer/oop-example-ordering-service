import re
from typing import Union, TYPE_CHECKING

from domain.model.base import PrimitiveValueObject


class Postcode(PrimitiveValueObject[str]):
    value_type = str

    @classmethod
    def _validate(cls, value):
        value = super()._validate(value)

        if not re.match(r'^\d{5}$', value):
            raise ValueError(f'Postcode must be a string of 5 digits, got {value}')

        return value

    if TYPE_CHECKING:
        def __init__(self, postcode: Union[str, 'Postcode']):
            super().__init__(...)
