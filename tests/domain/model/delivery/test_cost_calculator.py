import pytest

from domain.model import DomainRegistry
from domain.model.product import PriceThb
from domain.model.maps import MapsServiceAbstract, Address, DistanceKm

from domain.model.delivery import DeliveryCostCalculator


@pytest.fixture
def registry():
    reg = DomainRegistry()
    reg.reset()
    return reg


@pytest.fixture
def address_chiang_mai():
    return Address.build('123/4', 'ROAD', 'SUBDISTRICT', 'DISTRICT', 'chiang mai', '12345', 'THAILAND')


@pytest.fixture
def address_bangkok():
    return Address.build('123/4', 'ROAD', 'SUBDISTRICT', 'DISTRICT', 'bangkok', '12345', 'THAILAND')


@pytest.mark.asyncio
async def test_small_order_far_destination(registry, address_chiang_mai):
    class MapsDummy(MapsServiceAbstract):
        async def calculate_distance_from_warehouses(self, destination: Address) -> DistanceKm:
            return DistanceKm(50.0)

    registry.maps_service = MapsDummy()

    total_product_cost = PriceThb(20.0)
    result = await DeliveryCostCalculator.calculate_cost(total_product_cost, address_chiang_mai)

    assert result == PriceThb(350.0)


@pytest.mark.asyncio
async def test_small_order_near_destination(registry, address_chiang_mai):
    class MapsDummy(MapsServiceAbstract):
        async def calculate_distance_from_warehouses(self, destination: Address) -> DistanceKm:
            return DistanceKm(3.5)

    registry.maps_service = MapsDummy()

    total_product_cost = PriceThb(20.0)
    result = await DeliveryCostCalculator.calculate_cost(total_product_cost, address_chiang_mai)

    assert result == PriceThb(50.0)


@pytest.mark.asyncio
async def test_large_order_far_bangkok_destination(registry, address_bangkok):
    class MapsDummy(MapsServiceAbstract):
        async def calculate_distance_from_warehouses(self, destination: Address) -> DistanceKm:
            return DistanceKm(99999.999)

    registry.maps_service = MapsDummy()

    total_product_cost = PriceThb(1_000.0)
    result = await DeliveryCostCalculator.calculate_cost(total_product_cost, address_bangkok)

    assert result == PriceThb(0.0)


@pytest.mark.asyncio
async def test_large_order_near_bangkok_destination(registry, address_bangkok):
    class MapsDummy(MapsServiceAbstract):
        async def calculate_distance_from_warehouses(self, destination: Address) -> DistanceKm:
            return DistanceKm(5.3)

    registry.maps_service = MapsDummy()

    total_product_cost = PriceThb(500.0)
    result = await DeliveryCostCalculator.calculate_cost(total_product_cost, address_bangkok)

    assert result == PriceThb(0.0)


@pytest.mark.asyncio
async def test_large_order_near_chiang_mai_destination(registry, address_chiang_mai):
    class MapsDummy(MapsServiceAbstract):
        async def calculate_distance_from_warehouses(self, destination: Address) -> DistanceKm:
            return DistanceKm(10.0)

    registry.maps_service = MapsDummy()

    total_product_cost = PriceThb(500.0)
    result = await DeliveryCostCalculator.calculate_cost(total_product_cost, address_chiang_mai)

    assert result == PriceThb(0.0)


@pytest.mark.asyncio
async def test_large_order_far_chiang_mai_destination(registry, address_chiang_mai):
    class MapsDummy(MapsServiceAbstract):
        async def calculate_distance_from_warehouses(self, destination: Address) -> DistanceKm:
            return DistanceKm(10.00001)

    registry.maps_service = MapsDummy()

    total_product_cost = PriceThb(500.0)
    result = await DeliveryCostCalculator.calculate_cost(total_product_cost, address_chiang_mai)

    assert result == PriceThb(50.0)
