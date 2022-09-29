from abc import ABC, abstractmethod

from .component import Component


class ComponentFactory(ABC):
    @abstractmethod
    def create(self) -> Component:
        ...

    @abstractmethod
    def component_name(self) -> str:
        ...
