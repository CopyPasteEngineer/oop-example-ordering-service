from typing import Dict

from domain.model.base import ValueObject

from .address_entry import AddressEntry
from .postcode import Postcode
from .province import Province


class Address(ValueObject):
    def __init__(self, house_number: AddressEntry, road: AddressEntry, sub_district: AddressEntry,
                 district: AddressEntry, province: Province, postcode: Postcode, country: AddressEntry):
        self._house_number: AddressEntry = AddressEntry(house_number)
        self._road: AddressEntry = AddressEntry(road)
        self._sub_district: AddressEntry = AddressEntry(sub_district)
        self._district: AddressEntry = AddressEntry(district)
        self._province: Province = Province(province)
        self._postcode: Postcode = Postcode(postcode)
        self._country: AddressEntry = AddressEntry(country)

    @classmethod
    def build(cls, house_number: str, road: str, sub_district: str, district: str, province: str,
              postcode: str, country: str):
        return cls(AddressEntry(house_number), AddressEntry(road), AddressEntry(sub_district),
                   AddressEntry(district), Province(province), Postcode(postcode), AddressEntry(country))

    def bangkok_and_surrounding(self) -> bool:
        return self._province.bangkok_and_surrounding()

    @property
    def house_number(self) -> AddressEntry:
        return self._house_number

    def serialize(self) -> Dict:
        return {
            'house_number': self._house_number.serialize(),
            'road': self._road.serialize(),
            'sub_district': self._sub_district.serialize(),
            'district': self._district.serialize(),
            'province': self._province.serialize(),
            'postcode': self._postcode.serialize(),
            'country': self._country.serialize(),
        }

    @classmethod
    def deserialize(cls, value: Dict) -> 'Address':
        return cls(
            house_number=AddressEntry.deserialize(value.get('house_number')),
            road=AddressEntry.deserialize(value.get('road')),
            sub_district=AddressEntry.deserialize(value.get('sub_district')),
            district=AddressEntry.deserialize(value.get('district')),
            province=Province.deserialize(value.get('province')),
            postcode=Postcode.deserialize(value.get('postcode')),
            country=AddressEntry.deserialize(value.get('country')),
        )

    def __eq__(self, other):
        if isinstance(other, Address):
            return all([
                self._house_number == other._house_number,
                self._road == other._road,
                self._sub_district == other._sub_district,
                self._district == other._district,
                self._province == self._province,
                self._postcode == self._postcode,
                self._country == self._country,
            ])
        return False
