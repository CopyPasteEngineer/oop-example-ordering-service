from abc import ABC, abstractmethod

from domain.model.product import PriceThb

from .payment_id import PaymentId


class PaymentServiceAbstract(ABC):
    @abstractmethod
    async def new_payment(self, total_price: PriceThb) -> PaymentId:
        pass

    @abstractmethod
    async def verify_payment(self, payment_id: PaymentId) -> bool:
        pass
