"""Vamos a entender el patrón Simple Factory con la ayuda de un ejemplo de código Python . 
En el siguiente fragmento, creamos un producto abstracto llamado Animal. Animal es
una clase base abstracta (ABCMeta es la metaclase especial de Python para hacer una clase Abstracta)
y tiene el método do_say(). Creamos dos productos (Gato y Perro) a partir de la interfaz Animal
e implementamos do_say() con los sonidos apropiados que emiten estos animales.
ForestFactory es una fábrica que tiene el método make_sound(). 
En función del tipo de argumento pasado por el cliente, se crea en tiempo de ejecución una instancia 
de Animal apropiada y se imprime el sonido adecuado y se imprime el sonido adecuado:"""

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def dicen(self):
        pass

class Perro(Animal):
    def dicen(self):
        print("Gua Guau")

class Gato(Animal):
    def dicen(self):
        print("Miau miau")

#Fabrica
class SonidosFabrica(object):
    def hacer_sonido(self, object_type):
        return eval(object_type)().dicen()
    
#Cliente

if __name__ == '__main__':
    ff = SonidosFabrica()
    animal = input("Sonido de Gato o Perro:")
    ff.hacer_sonido(animal)

