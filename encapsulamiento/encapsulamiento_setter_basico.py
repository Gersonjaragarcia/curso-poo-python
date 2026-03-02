# Setter con validación
## Un carro pude tener modelo menor a 1880
class Carro:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.__modelo = modelo
        
    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, nuevo_modelo):
        if nuevo_modelo >= 1880:
            self.__modelo = nuevo_modelo 
            
        else:
            print("Modelo invalidado")
            
carro1 = Carro("Toyota", 2020)
carro1.set_modelo(1700) # Modelo invalidado
print(carro1.get_modelo())