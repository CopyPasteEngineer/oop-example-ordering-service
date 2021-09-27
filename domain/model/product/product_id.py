from typing import TYPE_CHECKING, Union

from domain.model.base import StrIdValueObject


class ProductId(StrIdValueObject):
    if TYPE_CHECKING:
        def __init__(self, id_: Union[str, 'ProductId']):
            super().__init__(...)
