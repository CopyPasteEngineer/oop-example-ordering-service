from abc import ABC, abstractmethod

from domain.model.product import PriceThb

from .payment_id import PaymentId


class PaymentServiceAbstract(ABC):
    @abstractmethod
    async def new_payment(self, total_price: PriceThb) -> PaymentId:
        pass
