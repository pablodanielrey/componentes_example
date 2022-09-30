from dv_pepe.models import Registry, ComponentSettings


def register_components(registry: Registry):
    """
    This needs to be executed when creating the system
    """
    general_settings = ComponentSettings(setting1=1, setting2="pepe")

    try:
        from dv_pepe.c1 import Factory, C1Settings

        c1_settings = C1Settings(setting1=10)

        registry.register(Factory(general_settings, c1_settings))

    except Exception:
        print("c1 no encontrado")

    try:
        from dv_pepe.c2 import Factory

        registry.register(Factory(general_settings))

    except Exception:
        print("c2 no encontrado")


def use_case(registry: Registry):
    """
    This executes in the user cases. for example and endpoint
    or a do_task from a loop.
    """
    for comp in registry.components():
        print(f"instanciando componente {comp}")
        componente = registry.get(comp)
        print(f"ejecutando componente {comp}")
        componente.do_something()


print("registrando componentes")
registry = Registry()
register_components(registry)
print(f"componentes registrados {registry.components()}")

print("usando los componentes")
use_case(registry)
