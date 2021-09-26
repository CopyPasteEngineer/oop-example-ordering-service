from typing import TypeVar
from abc import ABC, abstractmethod
from .serializable import Serializable


ImplementationType = TypeVar('ImplementationType', bound='ValueObject')


class ValueObject(Serializable, ABC):

    @abstractmethod
    def __eq__(self: ImplementationType, other: ImplementationType):
        pass
