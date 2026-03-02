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
        
    def get_modelo(self):
        return self.__modelo
        
carro1 = Carro("Toyota", 2020)
carro1.__modelo = 3000 # atrivuto creado por fuera

print(carro1.__modelo)
print(carro1.get_modelo())
