from typing import TYPE_CHECKING, Union

from domain.model.base import StrIdValueObject


class PaymentId(StrIdValueObject):
    if TYPE_CHECKING:
        def __init__(self, id_: Union[str, 'PaymentId']):
            super().__init__(...)
