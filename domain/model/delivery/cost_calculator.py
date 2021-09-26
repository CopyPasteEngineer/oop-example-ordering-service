from domain.model.maps import Address
from domain.model.product import PriceThb

from .large_order_cost_calculator import LargeOrderDeliveryCostCalculator
from .small_order_cost_calculator import SmallOrderDeliveryCostCalculator

ORDER_PRICE_THRESHOLD = PriceThb(500.0)


class DeliveryCostCalculator:
    @classmethod
    async def calculate_cost(cls, total_product_cost: PriceThb, destination: Address) -> PriceThb:
        if total_product_cost >= ORDER_PRICE_THRESHOLD:
            return await LargeOrderDeliveryCostCalculator.calculate_cost(destination)

        return await SmallOrderDeliveryCostCalculator.calculate_cost(destination)
