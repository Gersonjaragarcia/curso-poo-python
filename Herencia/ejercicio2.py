class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar_monto(self, monto):
        if monto > 0:
            self.saldo = self.saldo + monto
        else:
            print("No se puede depositar una cantidad negativa o cero")
            
    def retirar_monto(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo = self.saldo - monto
        else:
            print("No se puede retirar el dinero")
    
    def mostrar_info(self):
        print(f"Tu saldo actual es de: {self.saldo}")
        
class CuentaAhorro(CuentaBancaria):
    def __init__(self,titular, saldo, porcentaje):
        super().__init__(titular, saldo)
        self.porcentaje = porcentaje
        
    def aplicar_interes(self):
        if self.saldo > 0:
            self.saldo = self.saldo + (self.saldo * self.porcentaje )
            
    def mostrar_info(self):
        super().mostrar_info()
        
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, limite_descubierto):
        super().__init__(titular, saldo)
        self.limite_descubierto = limite_descubierto
    
    
    
    def retirar_monto(self, monto):
        if monto > 0:
            if  monto <= self.saldo + self.limite_descubierto:
                self.saldo = self.saldo - monto
                
            else:
                print("Mensaje de error")