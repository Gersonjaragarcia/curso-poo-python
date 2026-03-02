class Vehiculo:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.__velocidad = velocidad # atributo privado
    
    def get_velocidad(self):
        return self.__velocidad
    
    def set_velocidad(self, nueva_velocidad):
        if nueva_velocidad < 0:
            raise ValueError("La velocidad no puede ser negativa")
        self.__velocidad = nueva_velocidad 
        
class Moto(Vehiculo):
    def __init__(self, marca, velocidad, tipo):
        super().__init__(marca,velocidad)
        self.tipo = tipo 

moto1 = Moto("Yamaha", 120, "Deportiva")
print(moto1.get_velocidad())