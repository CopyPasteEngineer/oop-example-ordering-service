from typing import Union, TYPE_CHECKING

from domain.model.base import PrimitiveValueObject


class AddressEntry(PrimitiveValueObject[str]):
    value_type = str

    if TYPE_CHECKING:
        def __init__(self, value: Union[str, 'AddressEntry']):
            super().__init__(...)
