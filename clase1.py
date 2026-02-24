class Coche:
    def __init__(self, gasolina:int):
        self.gasolina = gasolina
        print("Tenemos", gasolina, "litros")
        
    def arrancar(self):
        if self.gasolina > 0:
            print("Arranca")
            
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -=1
            print("Quedan", self.gasolina, "Litros")
        else:
            print("No se mueve")
            
# Para crear el objeto
coche_1 = Coche(5)
coche_2 = Coche(7)

"""
Ahora que ya hemos creado nuestro objeto, podemos acceder a sus
atributos y métodos mediante la sintaxis objeto.atributo y objeto.
metodo():
"""
print(coche_1.gasolina)
coche_2.arrancar()
coche_2.conducir()