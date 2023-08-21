"""Considere el caso de su pizzería favorita. Sirve varios tipos de pizzas, ¿verdad?
Espera un momento, sé que quieres pedir una ahora mismo, pero volvamos al
ejemplo.
Ahora, imagina que creamos una pizzería donde te sirven deliciosas pizzas indias y 
americanas. Para ello, primero creamos una clase base abstracta, PizzaFactory
(AbstractFactory en el diagrama UML anterior). La clase PizzaFactory tiene dos métodos
métodos abstractos, createVegPizza() y createNonVegPizza(), que deben ser
implementados por ConcreteFactory. En este ejemplo, creamos dos fábricas concretas,
a saber, IndianPizzaFactory y USPizzaFactory. """

from abc import ABCMeta, abstractmethod

class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def crearVegPizza(self):
        pass

    @abstractmethod
    def crearNoVegPizza(self):
        pass

class IndianPizzaFactory(PizzaFactory):
    def crearVegPizza(self):
        return DeluxVeggiePizza()
    
    def crearNoVegPizza(self):
        return ChickenPizza()
    
class USPizzaFactory(PizzaFactory):
    def crearNoVegPizza(self):
        return HamPizza()
    
    def crearVegPizza(self):
        return MexicanVegPizza()

"""Ahora, avancemos y definamos AbstractProducts. En el siguiente código creamos
dos clases abstractas, VegPizza y NonVegPizza . Cada una de ellas tiene definido un método
Preparar() y Servir().
El proceso pensado aquí es que las pizzas vegetarianas se preparan con una corteza adecuada,
verduras y condimentos adecuados, y las pizzas no vegetarianas se sirven con aderezos
encima de las pizzas vegetarianas."""
        
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def preparar(self, VegPizza):
        pass

class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def servir(self, VegPizza):
        pass

class DeluxVeggiePizza(VegPizza):
    def preparar(self):
        print("Preparar : ", type(self).__name__)

class ChickenPizza(NonVegPizza):
    def servir(self, VegPizza):
        print(type(self).__name__, "servida con pollo", type(VegPizza).__name__)

class MexicanVegPizza(VegPizza):
    def preparar(self):
        print("Preparar : ", type(self).__name__)
        

class HamPizza(NonVegPizza):
    def servir(self, VegPizza):
        print(type(self).__name__, "servida con Jamón", type(VegPizza).__name__)


"""Cuando un usuario final se acerca a PizzaStore y pide una pizza americana no vegetariana,
USPizzaFactory se encarga de preparar la pizza vegetariana como base y de servir
la pizza no vegetariana con jamón por encima. """

class PizzaStore():

    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.crearNoVegPizza()
            self.VegPizza = self.factory.crearVegPizza()
            self.VegPizza.preparar()
            self.NonVegPizza.servir(self.VegPizza)
        

pizza = PizzaStore()
pizza.makePizzas()