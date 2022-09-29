from typing import Dict

from .component import Component
from .factory import ComponentFactory


class Registry:
    def __init__(self):
        self._factories: Dict[str, ComponentFactory] = {}

    def register(self, f: ComponentFactory):
        self._factories[f.component_name()] = f

    def get(self, name: str) -> Component:
        if name not in self._factories:
            raise Exception("Component not registered")
        return self._factories[name].create()

    def components(self):
        return self._factories.keys()
