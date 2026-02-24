"""
Docstring for ejercicio_polimorfismo:
🟢 1️⃣ Vehículos y Movimiento

    Clase base: Vehiculo

        atributo: marca

        método: mover()

    Clases hijas:

        Coche

        Bicicleta

        Avion

Cada una redefine mover().

👉 Crea una lista de vehículos y recórrela usando polimorfismo.
"""

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        
    def mover(self):
        print(f"el vehiculo {self.marca} se esta moviendo")
        
class Coche(Vehiculo):
    def __init__(self, marca):
        super().__init__(marca)
        
    def mover(self):
        print(f"el vehiculo {self.marca} se esta moviendo")
        
class Bicicleta(Vehiculo):
    def __init__(self, marca):
        super().__init__(marca)
        
    def mover(self):
        print(f"El vehiculo {self.marca} se esta moviendo")
        

vehiculo_1 = Vehiculo("Mazada")
coche_1 = Coche("Mercedez BEM")
bicicleta = Bicicleta("Bmx")

medios_trasportes = [vehiculo_1, coche_1, bicicleta]

for medios in medios_trasportes:
    medios.mover()