"""
Docstring for ejercicio2_polimorfismo:
 🟢 2️⃣ Sistema Escolar

    Clase base: Persona

        atributo: nombre

        método: mostrar_rol()

    Clases hijas:

        Estudiante

        Profesor

        Director

Cada una debe mostrar su rol diferente.
"""
class Persona:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
        
    def rol(self):
        print(f"Mi nombre es: {self.nombre} y soy una persona")
        
class Estudiantes(Persona):
    def __init__(self, nombre, profesion):
        super().__init__(nombre, profesion)
        
    def rol(self):
        print(f"Mi nombre es: {self.nombre} y soy un {self.profesion}")

class Profesor(Persona):
    def __init__(self, nombre, profesion):
        super().__init__(nombre, profesion)
        
    def rol(self):
        print(f"Mi nombre es: {self.nombre} y soy un {self.profesion}")
        
class Director(Persona):
    def __init__(self, nombre, profesion):
        super().__init__(nombre, profesion)
        
    def rol(self):
        print(f"Mi nombre es: {self.nombre} y soy un {self.profesion}")
        
# intanciar la clase 
persona1=Persona("Carlos", "Dev")
estudiante1= Estudiantes("Ana", "Estudiantes")
profesor1= Profesor("Mirian", "Profesor de matematicas")
director1= Director("Sebastian", "Director de ventas")

profesiones= [
    persona1,
    estudiante1,
    profesor1,
    director1
]

for a in profesiones:
    a.rol()