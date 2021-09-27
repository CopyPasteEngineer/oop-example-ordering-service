from typing import TYPE_CHECKING, Union

from domain.model.base import StrIdValueObject


class BuyerId(StrIdValueObject):
    if TYPE_CHECKING:
        def __init__(self, id_: Union[str, 'BuyerId']):
            super().__init__(...)
