class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        
        
    def mostrar_info(self):
        print(f"nombre: {self.nombre}")
        print(f"Slario: {self.salario}")
        
    def calcular_bono(self):
        return self.salario * 0.10
    
    def salario_total(self):
        return self.salario + self.calcular_bono()
        
class Gerente(Empleado):
    def __init__(self,nombre, salario, despartamento):
        super().__init__(nombre, salario) # llama al constructor del padre
        self.departamento = despartamento
        
    def mostrar_info(self):
        super().mostrar_info() # Usa el metodo del padre
        print(f"Departamento: {self.departamento}")
    
    def calcular_bono(self):
        return self.salario * 0.20
    
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguajes):
        super().__init__(nombre, salario)
        self.lenguaje = lenguajes 
        
    def mostrar_info(self):
        super().mostrar_info()
        print("fLenguajes principal: {self.lenguaje}")
        
    def calcular_bono(self):
        if self.lenguaje.lower() == "python":
            return self.salario * 0.15
        else:
            return self.salario * 0.10
        
empleado1 = Empleado("Carlos", 20000)
gerente1 = Gerente("Pedro", 3000, "Ventas")
dev1 = Desarrollador("Lucas", 40000, "python")

print("==== Empleado===")
empleado1.mostrar_info()

print("==== Gerente ===")
gerente1.mostrar_info()

print("==== desarrollador ===")
dev1.mostrar_info()

empleados = [
    Empleado("Carlos", 2000),
    Gerente("Ana", 5000, "Ventas"),
    Desarrollador("Luis", 3000, "Python"),
    Desarrollador("Sofía", 3000, "Java")
]

for e in empleados:
    print("\n--- Información ---")
    e.mostrar_info()
    print(f"Bono: ${e.calcular_bono()}")
    print(f"Salario total: ${e.salario_total()}")