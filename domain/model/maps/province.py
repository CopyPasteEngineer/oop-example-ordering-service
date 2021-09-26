from typing import Union
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
    Enum = ProvinceEnum

    def __init__(self, province: Union[str, 'Province']):
        value: str = self._validate(province)
        super().__init__(value)

    def bangkok_and_surrounding(self) -> bool:
        return self._value in _bangkok_and_surrounding_provinces

    @staticmethod
    def _validate(province):
        if isinstance(province, str):
            if not ProvinceEnum.has_value(province):
                raise ValueError(f'Province named "{province}" not exists')
            value = province
        elif isinstance(province, ProvinceEnum):
            value = province.value
        elif isinstance(province, Province):
            value = province._value
        else:
            raise TypeError(f'Expect value of type (str, Province), got {type(province)}')

        return value


_bangkok_and_surrounding_provinces = {
    ProvinceEnum.BANGKOK,
    ProvinceEnum.NAKHON_PATHOM,
    ProvinceEnum.NONTHABURI,
    ProvinceEnum.PATHUM_THANI,
    ProvinceEnum.SAMUT_PRAKAN,
    ProvinceEnum.SAMUT_SAKHON,
}
