"""Preparación de Pizza en pasos especificos"""

from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress','en_cola preparando en_horno lista')
PizzaDough = Enum('PizzaDough', 'Fina Gruesa')
PizzaSauce = Enum('PizzaSauce','tomate crema_fresca')
PizzaTopping = Enum('PizzaTopping', 'mozzarella doble_mozzarella tocino jamon champiñones cebolla oregano')
STEP_DELAY = 3


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
        
    def __str__(self):
        return self.name
    
    def prepare_dough(self, dough):
        self.dough = dough
        print("Preparando la {} masa de su {}".format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print("{} masa hecha satisfactoriamente".format(self.dough.name))


class MargaritaBuilder():
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.en_cola
        self.baking_time = 5
    
    def prepare_dough(self):
        self.progress = PizzaProgress.preparando
        self.pizza.prepare_dough(PizzaDough.Fina)

    def add_sauce(self):
        print("Agregando la salsa de tomate a su pizza margarita...")
        self.pizza.sauce = PizzaSauce.tomate
        time.sleep(STEP_DELAY)
        print("Salsa agregada satisfactoriamente")

    def add_topping(self):
        print("Agregando toppings (doble mozzarella y oregano) a su pizza margarita...")
        self.pizza.topping.append = ([i for i in (PizzaTopping.doble_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print("Toppings agregados satisfactoriamente...")

    def bake(self):
        print("Horneando su pizza margarita por {} segundos".format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress= PizzaProgress.lista
        print("Su pizza margarita esta lista")

class CreamyBaconBuilder():
    def __init__(self):
        self.pizza = Pizza('Creamy Bacon')
        self.progress = PizzaProgress.en_cola
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparando
        self.pizza.prepare_dough(PizzaDough.Gruesa)
    
    def add_sauce(self):
        print("Agregando Crema fresca a la pizza Creamy Beacon")
        self.pizza.sauce = PizzaSauce.crema_fresca
        time.sleep(STEP_DELAY)
        print("Crema fresca agregada satisfactoriamente...")

    def add_topping(self):
        print("Agregando toppings (mozzarella, tocino, jamon, champiñones, cebolla, oregano) a su pizza creamy bacon ...")
        self.pizza.topping.append([t for t in (PizzaTopping.mozzarella,PizzaTopping.tocino, PizzaTopping.jamon, PizzaTopping.cebolla, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print("Toppings agregados satisfactoriamente a la pizza creamy bacon")

    def bake(self):
        self.progress = PizzaProgress.en_horno
        print("Horneando su pizza creamy bacon por {} segundos".format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.lista
        print("Su pizza creamy bacon esta lista!")


#Clase directora

class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in(builder.prepare_dough, builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza



def validate_style(builders):
    try:
        pizza_style = input('Que pizza desea, [m]argarita or [c]reamy bacon? ')
        builder = builders[pizza_style]()
        validate_input = True
    except KeyError as err:
        print("Lo siento, solo margarita (m) and creamy bacon (c) estan disponibles ")
        return (False,None)
    return True, builder

def main():
    builders = dict(m=MargaritaBuilder,c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print("Disfruta tu {} pizza!".format(pizza))

if __name__ == '__main__':
    main()