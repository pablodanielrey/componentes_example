from dv_pepe.models import Component, ComponentFactory, ComponentSettings


class C2(Component):
    def __init__(self, settings: ComponentSettings):
        self._settings = settings

    def do_something(self):
        print("C2")
        print(f"Las settings generales son : {self._settings}")


class Factory(ComponentFactory):
    def __init__(self, settings: ComponentSettings):
        self._settings = settings

    def create(self) -> Component:
        return C2(self._settings)

    def component_name(self) -> str:
        return C2.__name__
