"""
Crea una clase Cuenta que tenga un atributo privado __saldo.

    Getter: get_saldo().
    Setter: depositar(monto) (solo si el monto es mayor a 0).
    Método Extra: retirar(monto) que reste al saldo solo si hay fondos suficientes. Si no, imprime un error.
    Objetivo: Practicar la lógica de control dentro de los métodos.
"""
class Cuenta:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial # Atributo privado
    
    # Getter para consultar el saldo
    def get_saldo(self):
        return self.__saldo
    
    # Método para depositar (actúa como un setter especial)
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto a depositar debe ser positivo.")

    # Método para retirar
    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Saldo restante: {self.__saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

# --- Prueba del código ---
mi_cuenta = Cuenta(1000)
print(f"Saldo inicial: {mi_cuenta.get_saldo()}")

mi_cuenta.depositar(500)
mi_cuenta.retirar(200)


