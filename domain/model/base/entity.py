from abc import ABC

from .serializable import Serializable
from .auto_serializer import AutoSerializerMixin, AutoSerializerMeta


class Entity(Serializable, ABC):
    pass


# class EntityAuto(AutoSerializerMixin, metaclass=AutoSerializerMeta):
#     pass
