import uuid

from domain.model.payment import PaymentServiceAbstract, PaymentId
from domain.model.product import PriceThb


class PayPalPaymentService(PaymentServiceAbstract):
    async def new_payment(self, total_price: PriceThb) -> PaymentId:
        return PaymentId(str(uuid.uuid4()))
