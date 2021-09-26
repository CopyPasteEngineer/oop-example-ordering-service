from domain.model.maps import Address


def test_address_build():
    Address.build('123/4', 'ROAD', 'SUBDISTRICT', 'DISTRICT', 'chiang mai', '12345', 'THAILAND')


def test_bangkok_and_surrounding_nonthaburi():
    address = Address.build('123/4', 'ROAD', 'SUBDISTRICT', 'DISTRICT', 'nonthaburi', '12345', 'THAILAND')
    assert address.bangkok_and_surrounding()


def test_bangkok_and_surrounding_chiang_mai():
    address = Address.build('123/4', 'ROAD', 'SUBDISTRICT', 'DISTRICT', 'chiang mai', '12345', 'THAILAND')
    assert not address.bangkok_and_surrounding()


def test_serialize():
    address = Address.build('123/4', 'ROAD', 'SUBDISTRICT', 'DISTRICT', 'chiang mai', '12345', 'THAILAND')
    expected = {
        'house_number': '123/4',
        'road': 'ROAD',
        'sub_district': 'SUBDISTRICT',
        'district': 'DISTRICT',
        'province': 'chiang mai',
        'postcode': '12345',
        'country': 'THAILAND',
    }
    assert address.serialize() == expected


def test_deserialize():
    raw = {
        'house_number': '123/4',
        'road': 'ROAD',
        'sub_district': 'SUBDISTRICT',
        'district': 'DISTRICT',
        'province': 'chiang mai',
        'postcode': '12345',
        'country': 'THAILAND',
    }
    expected = Address.build('123/4', 'ROAD', 'SUBDISTRICT', 'DISTRICT', 'chiang mai', '12345', 'THAILAND')
    assert Address.deserialize(raw) == expected
