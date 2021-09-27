from typing import Union, TYPE_CHECKING
from enum import Enum

from domain.model.base import PrimitiveValueObject


class ProvinceEnum(str, Enum):
    BANGKOK: str = 'bangkok'
    NAKHON_PATHOM: str = 'nakhon pathom'
    NONTHABURI: str = 'nonthaburi'
    PATHUM_THANI: str = 'pathum thani'
    SAMUT_PRAKAN: str = 'samut prakan'
    SAMUT_SAKHON: str = 'samut sakhon'
    CHIANG_MAI: str = 'chiang mai'

    @classmethod
    def has_value(cls, value):
        return value in cls._member_map_.values()


class Province(PrimitiveValueObject[str]):
    value_type = str
    Enum = ProvinceEnum

    def bangkok_and_surrounding(self) -> bool:
        return self._value in _bangkok_and_surrounding_provinces

    @classmethod
    def _validate(cls, value):
        if isinstance(value, ProvinceEnum):
            value = value.value
        value = super()._validate(value)

        if not ProvinceEnum.has_value(value):
            raise ValueError(f'Province named "{value}" not exists')

        return value

    if TYPE_CHECKING:
        def __init__(self, value: Union[str, 'Province']):
            super().__init__(...)


_bangkok_and_surrounding_provinces = {
    ProvinceEnum.BANGKOK,
    ProvinceEnum.NAKHON_PATHOM,
    ProvinceEnum.NONTHABURI,
    ProvinceEnum.PATHUM_THANI,
    ProvinceEnum.SAMUT_PRAKAN,
    ProvinceEnum.SAMUT_SAKHON,
}
