from domain.model.maps import MapsServiceAbstract, Address, DistanceKm


class GoogleMapsService(MapsServiceAbstract):
    async def calculate_distance_from_warehouses(self, destination: Address) -> DistanceKm:
        house_number = str(destination.house_number).split('/')[0]
        return DistanceKm(float(house_number))
