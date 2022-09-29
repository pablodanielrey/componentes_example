from dv_pepe.models import Component
from dv_pepe.models import ComponentFactory


class C1(Component):
    def do_something(self):
        print("C1")


class Factory(ComponentFactory):
    def create(self) -> Component:
        return C1()

    def component_name(self) -> str:
        return C1.__name__
