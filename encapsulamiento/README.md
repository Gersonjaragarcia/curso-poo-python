## ¿Por qué encapsular?
Primero hay que entender esto:
Una clase de payton tiene: atributos y comprtamientos  o tambien se llaman metodos
El problema es cuando alguien modifica los datos sin control.

Ejemplo SIN encapsular:
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
el problema se encuntra cuando:

p = Persona("Ana", 20)
p.edad = -100

## ¿Qué hace realmente __?
_Carro__modelo
Esto se llama name mangling.

## NIVEL 1.1 — Getter (obtener valor)
Si algo es privado, necesitas una forma controlada de leerlo:
