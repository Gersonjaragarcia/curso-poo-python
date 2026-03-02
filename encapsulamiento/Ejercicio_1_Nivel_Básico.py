"""
Ejercicio 1  Nivel Básico

Crea:

Clase padre: Empleado

atributo privado: __salario

getter y setter con validación (no puede ser negativo)

Clase hija: Gerente

método sobrescrito: mostrar_info()
"""

class Empleado:
    def __init__(self,nombre, salario):
        self.nombre = nombre
        self.__salario = salario #encapsulado
        
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, nuevo_salario):
        if nuevo_salario < 0:
            raise ValueError("El monto del salario no puede ser negativo")
        self.__salario = nuevo_salario 
    
    def mostrar_info(self):
        print(f"El salario del empleado {self.nombre} es {self.get_salario()}")
        
class Gerente(Empleado):
    def mostrar_info(self):
        print(f"El salario del señor @ {self.nombre} es {self.get_salario()}")
        
empleado = [
    Empleado("Diana", 20000),
    Gerente("Carolina", 30000)
]

for e in empleado:
    e.mostrar_info()