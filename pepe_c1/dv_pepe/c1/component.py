from dataclasses import dataclass
from dv_pepe.models import Component, ComponentFactory, ComponentSettings


@dataclass
class C1Settings:
    setting1: int


class C1(Component):
    def __init__(self, settings: ComponentSettings, c1_settings: C1Settings):
        self._settings = settings
        self._c1_settings = c1_settings

    def do_something(self):
        print("C1")
        print(f"Las settings generales son : {self._settings}")
        print(f"Settings específicas de mi componente {self._c1_settings}")


class Factory(ComponentFactory):
    def __init__(self, settings: ComponentSettings, c1_settings: C1Settings):
        self._settings = settings
        self._c1_settings = c1_settings

    def create(self) -> Component:
        return C1(self._settings, self._c1_settings)

    def component_name(self) -> str:
        return C1.__name__
