from abc import ABC, abstractmethod

from .address import Address
from .distance_km import DistanceKm


class MapsServiceAbstract(ABC):
    @abstractmethod
    async def calculate_distance_from_warehouses(self, destination: Address) -> DistanceKm:
        pass
