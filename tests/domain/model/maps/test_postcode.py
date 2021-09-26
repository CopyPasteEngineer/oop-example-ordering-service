import pytest
from domain.model.maps import Postcode


def test_postcode_string():
    Postcode('10120')


def test_postcode_postcode():
    original = Postcode('10120')
    new = Postcode(original)
    assert original == new


def test_postcode_wrong_type():
    with pytest.raises(TypeError):
        Postcode(10120)


def test_postcode_wrong_pattern():
    with pytest.raises(ValueError):
        Postcode('a2cd0')
