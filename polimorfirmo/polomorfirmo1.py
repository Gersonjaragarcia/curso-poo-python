class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hacer_sonido(self):
        print("Soy un", self.nombre, "y este es mi sonido")
        
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def hacer_sonido(self):
        print("Soy un gato y este e smi sonido: miua")
        
class Perro(Animal):
    def __init__ (self, nombre):
        super().__init__(nombre)
        
    def hacer_sonido(self):
        print("Soy un perro y este es mi sonido:guau guau")
        
class Loro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def hacer_sonido(self):
        print("Sooy un loro y mi sonido es: corororro")
        
# intanciar la clase 
gato1 = Gato("Michi")
perro1 = Perro("Firulais")
loro1 = Loro("Piolín")
animal1 = Animal("Desconocido")

animales = [gato1, perro1, loro1, animal1]

for animal in animales:
    animal.hacer_sonido()
