from dv_pepe.models import Registry


def register_components(registry: Registry):
    try:
        from dv_pepe.c1 import Factory

        registry.register(Factory())

    except Exception:
        print("c1 no encontrado")

    try:
        from dv_pepe.c2 import Factory

        registry.register(Factory())

    except Exception:
        print("c2 no encontrado")


print("registrando componentes")
registry = Registry()
register_components(registry)
print(f"componentes registrados {registry.components()}")

print("usando los componentes")
for comp in registry.components():
    print(f"instanciando componente {comp}")
    componente = registry.get(comp)
    print(f"ejecutando componente {comp}")
    componente.do_something()
