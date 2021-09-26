from typing import Dict, Any
from functools import partial


class Attribute:
    pass


def validate(value, type_):
    if not isinstance(value, type_):
        deserialize = getattr(type_, 'deserialize', None)
        if deserialize:
            value = deserialize(value)
        else:
            value = type_(value)
    return value


def getter(self, name):
    return getattr(self, name)


def setter(self, value, name, type_):
    value = validate(value, type_)
    return setattr(self, name, value)


class AutoSerializerMeta(type):
    def __new__(mcs, class_name, bases, dct: Dict):
        annotations: Dict[str, type] = dct.get('__annotations__', {})
        attrs = {}
        slots = []
        for name, annotation in annotations.copy().items():
            if name.startswith('_'):
                continue

            attr = dct.get(name)
            if attr and isinstance(attr, Attribute):
                getter_name = name
                setter_name = f'_{name}'
                slot_name = f'_attr__{name}'

                prop = property(partial(getter, name=slot_name))
                dct[getter_name] = prop
                dct[setter_name] = prop.setter(partial(setter, name=slot_name, type_=annotation))
                attrs[getter_name] = attr
                slots.append(slot_name)

        dct['__attrs'] = attrs
        dct['__slots__'] = slots
        return super().__new__(mcs, class_name, bases, dct)


def serialize_value(value):
    if hasattr(value, 'serialize'):
        return value.serialize()
    return value


def deserialize_value(value):
    if hasattr(value, 'deserialize'):
        return value.deserialize()
    return value


class AutoSerializerMixin:
    _attrs: Dict[str, Attribute]
    _values: Dict[str, Any]

    def __init__(self, **kwargs):
        values = set()

        attrs = getattr(self, '__attrs')
        for name, value in kwargs.items():
            attr = attrs.get(name)
            if not attr:
                raise NameError(f'No attribute named {name}')

            setattr(self, f'_{name}', value)

            values.add(name)

        k_set = set(attrs.keys())
        if values != k_set:
            requires = k_set - values
            raise AttributeError(f'Attribute {requires} required')

    def serialize(self):
        return {name: serialize_value(getattr(self, name)) for name in getattr(self, '__attrs').keys()}

    @classmethod
    def deserialize(cls, data: Dict):
        return cls(**{key: deserialize_value(value) for key, value in data.items()})
