from typing import List, Union, Dict, Iterable

from domain.model.base import ValueObject

from domain.model.product import ProductId

from .amount import OrderAmount


class OrderLine(ValueObject):
    def __init__(self, product_id: ProductId, amount: OrderAmount):
        self._product_id: ProductId = ProductId(product_id)
        self._amount: OrderAmount = OrderAmount(amount)

    @property
    def product_id(self) -> ProductId:
        return self._product_id

    @property
    def amount(self) -> OrderAmount:
        return self._amount

    def __eq__(self, other):
        if not isinstance(other, OrderLine):
            return False

        return all([
            self._amount == other._amount,
            self._product_id == other._product_id,
        ])

    def serialize(self):
        return {
            'product_id': self._product_id.serialize(),
            'amount': self._amount.serialize(),
        }

    @classmethod
    def deserialize(cls, value: Dict) -> 'OrderLine':
        product_id = ProductId.deserialize(value['product_id'])
        amount = OrderAmount.deserialize(value['amount'])

        return cls(product_id=product_id, amount=amount)


class OrderLineList(ValueObject):
    def __init__(self, order_lines: Union[List[OrderLine], 'OrderLineList']):
        order_lines = self._validate_lines(order_lines)
        self._lines: List[OrderLine] = order_lines

    @staticmethod
    def _validate_lines(order_lines) -> List[OrderLine]:
        result = []
        for line in order_lines:
            if isinstance(line, OrderLine):
                result.append(line)
            else:
                raise TypeError(f'Expect value of type List[OrderLine], got List[{type(line)}]')

        return result

    def __iter__(self) -> Iterable[OrderLine]:
        for line in self._lines:
            yield line

    def __eq__(self, other):
        if not isinstance(other, OrderLineList):
            return False

        for self_line, other_line in zip(self._lines, other._lines):
            if self_line != other_line:
                return False

        return True

    def serialize(self) -> List:
        return [line.serialize() for line in self._lines]

    @classmethod
    def deserialize(cls, value: List) -> 'OrderLineList':
        return cls([OrderLine.deserialize(line) for line in value])
