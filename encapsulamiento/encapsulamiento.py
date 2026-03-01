class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Diana", 30)
p.edad= -100
print(p.edad)

#Ahora encapsulemos creemos una nueva clase y protegemos el atributo modelo

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.__modelo = modelo  # atributo privado
        
carro1 = Carro("Toyota", 2020)
