from typing import TYPE_CHECKING

from domain.model.base import ValueObject, ValueObjectList
from domain.model.base.model import Attribute, AttributeSetter

from domain.model.product import ProductId

from .amount import OrderAmount


class OrderLine(ValueObject):
    product_id: ProductId = Attribute()
    amount: OrderAmount = Attribute()

    if TYPE_CHECKING:
        def __init__(self, *, product_id: ProductId, amount: OrderAmount):
            super().__init__()

    _product_id: ProductId = AttributeSetter()
    _amount: OrderAmount = AttributeSetter()


class OrderLineList(ValueObjectList[OrderLine]):
    value_type = OrderLine
