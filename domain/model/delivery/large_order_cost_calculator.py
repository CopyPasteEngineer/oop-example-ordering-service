from domain.model.registry import DomainRegistry

from domain.model.maps import Address, DistanceKm
from domain.model.product import PriceThb


FREE_DISTANCE_THRESHOLD = DistanceKm(10.0)
FREE = PriceThb(0.0)
FLAT_PRICE = PriceThb(50.0)


class LargeOrderDeliveryCostCalculator:
    @classmethod
    async def calculate_cost(cls, destination: Address) -> PriceThb:
        distance_from_warehouse = await DomainRegistry().maps_service.calculate_distance_from_warehouses(destination)

        if destination.bangkok_and_surrounding() or distance_from_warehouse <= FREE_DISTANCE_THRESHOLD:
            return FREE

        return FLAT_PRICE
