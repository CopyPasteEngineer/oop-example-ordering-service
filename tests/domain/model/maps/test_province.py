import pytest
from domain.model.maps import Province


def test_province_string():
    Province('bangkok')


def test_province_enum():
    Province(Province.Enum.BANGKOK)


def test_province_province():
    original = Province('bangkok')
    new = Province(original)
    assert original == new


def test_province_wrong_type():
    with pytest.raises(TypeError):
        Province(1234)


def test_province_typo():
    with pytest.raises(ValueError):
        Province('bangcok')


def test_bangkok_and_surrounding_bangkok():
    assert Province('bangkok').bangkok_and_surrounding()


def test_bangkok_and_surrounding_pathum_thani():
    assert Province('pathum thani').bangkok_and_surrounding()


def test_bangkok_and_surrounding_chiang_mai():
    assert not Province('chiang mai').bangkok_and_surrounding()
