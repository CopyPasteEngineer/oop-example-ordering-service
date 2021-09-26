from typing import TypeVar, Generic
from abc import abstractmethod

from .str_id import StrIdValueObject
from .entity import Entity

IdType = TypeVar('IdType', bound=StrIdValueObject)
EntityType = TypeVar('EntityType', bound=Entity)


class EntityNotFound(Exception):
    pass


class EntityOutdated(Exception):
    pass


class RepositoryAbstract(Generic[IdType, EntityType]):
    @abstractmethod
    async def next_identity(self) -> IdType:
        pass

    @abstractmethod
    async def from_id(self, id_: IdType) -> EntityType:
        pass

    @abstractmethod
    async def save(self, entity: EntityType):
        pass
