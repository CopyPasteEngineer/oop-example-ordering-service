from domain.model.registry import DomainRegistry

from domain.model.maps import Address, DistanceKm
from domain.model.product import PriceThb

BASE_PRICE = PriceThb(50.0)
FREE_DISTANCE_THRESHOLD = DistanceKm(30.0)
PRICE_PER_EXTRA_DISTANCE = PriceThb(15.0)


class SmallOrderDeliveryCostCalculator:
    @classmethod
    async def calculate_cost(cls, destination: Address) -> PriceThb:
        distance_from_warehouse = await DomainRegistry().maps_service.calculate_distance_from_warehouses(destination)

        if distance_from_warehouse <= FREE_DISTANCE_THRESHOLD:
            return BASE_PRICE

        distance_extra = distance_from_warehouse - FREE_DISTANCE_THRESHOLD
        cost_extra = PRICE_PER_EXTRA_DISTANCE * distance_extra

        return PriceThb(BASE_PRICE + cost_extra)
