"""Consideremos que queremos crear perfiles de distintos tipos en redes sociales como LinkedIn 
y Facebook para una persona o empresa. Ahora bien, cada uno de estos perfiles tendría determinadas 
secciones. En LinkedIn, tendríamos una sección sobre las patentes que una persona ha presentado o 
las publicaciones que ha escrito. En Facebook, vería secciones en un álbum de fotos de su reciente
visita a un lugar de vacaciones. Además, en ambos perfiles, habría de haber una sección común de 
información personal. 
Así que, en resumen, queremos crear perfiles de diferentes tipos con las secciones adecuadas añadidas
al perfil. Veamos ahora la implementación. En el siguiente ejemplo de código, empezaremos
definiendo la interfaz Producto. Crearemos una clase abstracta Section que define
cómo será una sección. Lo mantendremos muy simple y proporcionaremos un método abstracto
describir().
Ahora creamos varias clases ConcreteProduct, PersonalSection, AlbumSection,
PatentSection, y PublicationSection. Estas clases implementan el método abstracto describe()
e imprimen los nombres de sus respectivas secciones:"""

from abc import ABCMeta, abstractmethod

class Seccion(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class SeccionPersonal(Seccion):
    def describe(self):
        print("Sección Personal")

class SeccionAlbum(Seccion):
    def describe(self):
        print("Sección Albumes")

class SeccionPatentes(Seccion):
    def describe(self):
        print ("Sección Patentes")

class SeccionPublicaciones(Seccion):
    def describe(self):
        print("Sección publicaciones")


"""Creamos una clase abstracta Creador que se llama Perfil. La clase abstracta Profile [Creator]
proporciona un método de fábrica, createProfile(). El método createProfile()
debe ser implementado por ConcreteClass para crear realmente los perfiles con
secciones apropiadas. La clase abstracta Profile no es consciente de las secciones que cada
perfil debe tener. Por ejemplo, un perfil de Facebook debe tener información personal
y secciones de álbum. Así que dejaremos que la subclase decida esto.
Creamos dos clases ConcreteCreator, linkedin y facebook. Cada una de estas clases
implementan el método abstracto createProfile() que en realidad crea (instancia)
múltiples secciones (ConcreteProducts) en tiempo de ejecución:"""

class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.secciones = []
        self.crearPerfil()
    
    @abstractmethod
    def crearPerfil(self):
        pass

    def getSecciones(self):
        return self.secciones
    
    def addSecciones(self,section):
        self.secciones.append(section)

class linkedin(Profile):
    def crearPerfil(self):
        self.addSecciones(SeccionPersonal())
        self.addSecciones(SeccionPatentes())
        self.addSecciones(SeccionPublicaciones())

class facebook(Profile):
    def crearPerfil(self):
        self.addSecciones(SeccionPersonal)
        self.addSecciones(SeccionAlbum)
    
if __name__=='__main__':
    profile_type= input("Que perfil va a crear [linkedin o Facebook]:")
    profile = eval(profile_type.lower())()
    print("Creando Perfil...", type(profile).__name__)
    print("Secciones del Perfil creado--", profile.getSecciones())
