
class HealthCheck:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instancia:
            HealthCheck._instancia = super(HealthCheck,cls).__new__(cls, *args,**kwargs)
        return HealthCheck._instancia

    def __init__(self):
        self._servers =[]

    def addServer(self):
        self._servers.append("Servidor 1")
        self._servers.append("Servidor 2")
        self._servers.append("Servidor 3")
        self._servers.append("Servidor 4")
    
    def changeServer(self):
        self._servers.pop()
        self._servers.append("Servidor 5")


h1 = HealthCheck()
h2 = HealthCheck()

h1.addServer()

print("Cronograma de servidores (1)..")

for i in range (4):
    print("Checking..", h1._servers[i])


h2.changeServer()

print("Cronograma de servidores (2)..")

for i in range (4):
    print("Checking..", h2._servers[i])
