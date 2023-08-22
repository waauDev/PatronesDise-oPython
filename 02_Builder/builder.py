"""La nueva analogía informática puede ayudar a distinguir entre un patrón Builder y un patrón Factory.
Supongamos que quiere comprar un ordenador nuevo. Si decide preconfigurado, por ejemplo, el último Mac
mini de Apple a 1,4 GHz, utilizará el patrón Fábrica.
Todas las especificaciones de hardware ya están predefinidas por el fabricante, que sabe qué 
hacer sin consultarte. El fabricante suele recibir una única instrucción. :"""

MINI14 ='MAC MINI'


class AppleFactory:
    class MacMini:
        def __init__(self):
            self.memory =4 #en gigabytes
            self.hdd = 500 # 
            self.gpu = 'Intel HD Graphics'

        
        def __str__(self):
            info = ( 'Model:{}'.format(MINI14),
                    'Memory:{}'.format(self.memory),
                    'Hard Disk:{}'.format(self.hdd),
                    'Graphics Card: {}'.format(self.gpu)
            )
            return '\n'.join(info)
        
    def build_computer(self, model):
        if(model==MINI14):
            return self.MacMini()
        else:
            print("No se como construir el {}").format(model)

if __name__=='__main__':
    afac = AppleFactory()
    mac_mini =afac.build_computer(MINI14)
    print(mac_mini)

"""Otra opción es comprar un PC a medida. En este caso, utilizas el patrón Constructor.
Usted es el director que da órdenes al fabricante (constructor) sobre las especificaciones
de tu ordenador ideal. Desde el punto de vista del código, esto se parece a lo siguiente
"""

print("Implementando Patron builder")

class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None
    
    def __str__(self):
        info = ('Serial:{}'.format(self.serial),
                'Memory:{}'.format(self.memory),
                'Hard Disk:{} GB'.format(self.hdd),
                'Graphics Card:{}'.format(self.gpu)
        )
        return '\n'.join(info)
    
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('ABCDX123')

    def configure_memory(self, amount):
        self.computer.memory= amount
    
    def configure_hdd(self, amount):
        self.computer.hdd = amount
    
    def configure_gpu(self, gpu_model):
        self.computer.gpu=gpu_model
    
class HardwareEngineer:
    def __init__(self):
        self.builder = None
    
    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory),
                           self.builder.configure_hdd(hdd),
                           self.builder.configure_gpu(gpu)
                           )]
    @property
    def computer(self):
        return self.builder.computer

def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500,memory=8,gpu='GForce')
    computer = engineer.computer
    print(computer)

if __name__=='__main__':
    main()