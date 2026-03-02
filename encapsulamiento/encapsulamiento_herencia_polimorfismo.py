class Vehiculo:
    
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.__velocidad = velocidad # encapsulado 
    
    def get_velocidad(self):
        return self.__velocidad
    
    def set_velocidad(self, nueva_velocidad):
        if nueva_velocidad < 0:
            raise ValueError("La velocidad no puede ser negativa")
        self.__velocidad = nueva_velocidad 
    
    def mover(self):
        print("El vihiculo se esta moviendo")  
    
class Carro(Vehiculo):
    def mover(self):
        print(f"El carro {self.marca} avanza por la carretera a {self.get_velocidad()}km")
        
class Avion(Vehiculo):
    def mover(self):
        print(f"El avion {self.marca} vuela a {self.get_velocidad()}")
        
class Bicicleta(Vehiculo):
    def mover(self):
        print(f"La bicicleta de {self.marca} alcanza una velocidad de {self.get_velocidad()}")
        
# Polimorfismo
vehiculo = [
    Carro("Toyota", 120),
    Avion("Boing", 800),
    Bicicleta("BMX", 100)
]

for v in vehiculo:
    v.mover()