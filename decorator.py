from abc import ABC, abstractmethod


class Component(ABC):
    """
    Defina la interfaz para los objetos que pueden tener responsabilidades agregadas dinámicamente
    """

    @abstractmethod
    def operation(self):
        pass


class Decorator(Component):
    """
    Mantenga una referencia a un objeto de componente y defina una interfaz que se ajuste a la interfaz de componente
    """

    def __init__(self, component):
        self._component = component

    @abstractmethod
    def operation(self):
        pass


class ConcreteDecoratorA(Decorator):
    """
    Agrega responsabilidades al componente
    """

    def operation(self):
        # Agrega funcionalidad antes de ejecutar la operacion
        self._component.operation()
        # Agrega funcionalidad despues de ejecutar la operacion


class ConcreteDecoratorB(Decorator):
    """
    Agrega responsabilidades al componente
    """

    def operation(self):
        # Agrega funcionalidad antes de ejecutar la operacion
        self._component.operation()
        # Agrega funcionalidad despues de ejecutar la operacion


class ConcreteComponent(Component):
    """
    Defina un objeto al cual nuevas responsabilidades pueden ser agregadas
    """

    def operation(self):
        pass


def main():
    concrete_component = ConcreteComponent()
    concrete_decorator_a = ConcreteDecoratorA(concrete_component)
    concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)
    concrete_decorator_b.operation()


if __name__ == "__main__":
    main()
