from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def do_something(self):
        ...
