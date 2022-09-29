from dv_pepe.models import Component
from dv_pepe.models import ComponentFactory


class C2(Component):
    def do_something(self):
        print("C2")


class Factory(ComponentFactory):
    def create(self) -> Component:
        return C2()

    def component_name(self) -> str:
        return C2.__name__
