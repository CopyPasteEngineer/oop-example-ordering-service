from typing import TYPE_CHECKING, Union

from domain.model.base import StrIdValueObject


class OrderId(StrIdValueObject):
    if TYPE_CHECKING:
        def __init__(self, id_: Union[str, 'OrderId']):
            super().__init__(...)
