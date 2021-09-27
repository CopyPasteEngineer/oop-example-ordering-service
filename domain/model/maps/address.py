from typing import TYPE_CHECKING

from domain.model.base import ValueObject
from domain.model.base.model import Attribute, AttributeSetter

from .address_entry import AddressEntry
from .postcode import Postcode
from .province import Province


class Address(ValueObject):
    house_number: AddressEntry = Attribute()
    road: AddressEntry = Attribute()
    sub_district: AddressEntry = Attribute()
    district: AddressEntry = Attribute()
    province: Province = Attribute()
    postcode: Postcode = Attribute()
    country: AddressEntry = Attribute()

    @classmethod
    def build(cls, house_number: str, road: str, sub_district: str, district: str, province: str,
              postcode: str, country: str):
        return cls(house_number=AddressEntry(house_number), road=AddressEntry(road),
                   sub_district=AddressEntry(sub_district), district=AddressEntry(district),
                   province=Province(province), postcode=Postcode(postcode), country=AddressEntry(country))

    def bangkok_and_surrounding(self) -> bool:
        return self._province.bangkok_and_surrounding()

    if TYPE_CHECKING:
        def __init__(self, house_number: AddressEntry, road: AddressEntry, sub_district: AddressEntry,
                     district: AddressEntry, province: Province, postcode: Postcode, country: AddressEntry):
            super().__init__()

    _house_number: AddressEntry = AttributeSetter()
    _road: AddressEntry = AttributeSetter()
    _sub_district: AddressEntry = AttributeSetter()
    _district: AddressEntry = AttributeSetter()
    _province: Province = AttributeSetter()
    _postcode: Postcode = AttributeSetter()
    _country: AddressEntry = AttributeSetter()
