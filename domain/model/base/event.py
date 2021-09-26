from typing import Dict
from abc import ABC, abstractmethod


class DomainEvent(ABC):
    @classmethod
    def event_name(cls):
        return cls.__name__

    @abstractmethod
    def serialize(self) -> Dict:
        pass


class DomainEventPublisher(ABC):
    @abstractmethod
    def publish(self, event: DomainEvent):
        pass


class DummyEventPublisher(DomainEventPublisher):
    def __init__(self):
        self.events = []

    def publish(self, event: DomainEvent):
        self.events.append(event)
