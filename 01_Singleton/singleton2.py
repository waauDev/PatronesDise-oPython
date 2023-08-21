"""Consideremos otro escenario en el que implementamos servicios de comprobación de la salud (como
Nagios) para nuestra infraestructura. Creamos la clase HealthCheck, que se implementa como
un Singleton. 
También mantenemos una lista de servidores contra los que debe ejecutarse el chequeo.
Si se elimina un servidor de esta lista, el software de comprobación de estado debe 
detectarlo y eliminarlo de los servidores configurados para comprobar.
de los servidores configurados para comprobar.

En el código , los objetos hc1 y hc2 son los mismos que la clase en Singleton.
Los servidores se añaden a la infraestructura para el chequeo con el método addServer().
Primero, la iteración del chequeo se ejecuta contra estos servidores. El método changeServer()
elimina el último servidor y añade uno nuevo a la infraestructura programada para el
chequeo. Así, cuando el chequeo se ejecuta en la segunda iteración, recoge la lista de servidores modificada.
lista de servidores modificada.
Todo esto es posible con Singletons. Cuando se añaden o eliminan servidores, el health check
debe ser el mismo objeto que tiene el conocimiento de los cambios realizados en la
infraestructura:"""

import sqlite3


class MetaSingleton(type):
    _instancias = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            cls._instancias[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instancias[cls]
    

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj
    

db1 = Database().connect

db2 = Database().connect


print ("Database Objects DB1", db1)
print ("Database Objects DB2", db2)
