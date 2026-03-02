# Curso de Programación Orientada a Objetos (POO) en Python

Bienvenido al curso de **Programación Orientada a Objetos (POO)**. Este repositorio documenta el aprendizaje de los pilares fundamentales para crear software organizado, seguro y escalable utilizando Python.

---

## Contenido
1. [Nivel 1: Clases y Objetos](#nivel-1--fundamentos-de-clases-y-objetos)
2. [Nivel 2: Encapsulamiento](#nivel-2--encapsulamiento)
3. [Nivel 3: Herencia](#nivel-3--herencia)
4. [Nivel 4: Polimorfismo](#nivel-4--polimorfismo)
5. [🚀 Proyecto Integrador](#-proyecto-integrador-sistema-de-empleados)
6. [🛠️ Ejercicios de Práctica](#-ejercicios-de-práctica)

---

##  Nivel 1 – Fundamentos de Clases y Objetos

### ¿Qué es una clase?
Una **clase** es una plantilla para crear objetos. Define:
- **Atributos** → Datos (Variables).
- **Métodos** → Comportamientos (Funciones).

#### Ejemplo básico:
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

# Crear objeto (Instanciación)
p1 = Persona("Ana", 22)
p1.saludar()

## Nivel 2 – Encapsulamiento
El encapsulamiento consiste en proteger los datos internos de un objeto para evitar modificaciones accidentales o incorrectas desde fuera de la clase.

    Atributos Privados: Usamos doble guion bajo (__atributo).
    Métodos Getter: Para obtener el valor de forma segura.
    Métodos Setter: Para modificar el valor aplicando reglas de validación.