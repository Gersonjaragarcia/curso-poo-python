class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hacer_sonido(self):
        print("soy un", self.nombre, "y este es mi sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print("Soy un peroo y hago: guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Soy un gato y hago: Miau")

# Instanciar los objetos
perro1= Perro("muñeco")
gato1 = Gato("Tito")

perro1.hacer_sonido()
gato1.hacer_sonido()

