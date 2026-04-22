class Persona:
    def __init__(self,nombre,apellido,dni):
        self.nombre = str(nombre)
        self.apellido = str(apellido)
        self.dni = str(dni)
    
    def mostrar_info(self):
        print("\nNombre: " + self.nombre)
        print("Apellido: " + self.apellido)
        print("DNI: " + self.dni + "\n")
    
class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = int(saldo)
    
    def ingresar(self,cantidad):
        self.saldo = self.saldo + cantidad
        print("\nSe ha aumentado el saldo, saldo actual: " + str(self.saldo) + "€")
    
    def retirar(self,cantidad):
        if self.saldo < cantidad:
            print("\nSaldo insuficiente.")
        else:
            self.saldo = self.saldo - cantidad
            print("\nSe ha retirado: " + str(cantidad) + "€, saldo actual: " + str(self.saldo) + "€")
    
    def mostrar_info(self):
        print("\n== INFO. DEL TITULAR ==")
        self.titular.mostrar_info()
        print("Saldo: " + str(self.saldo) + "€\n")

persona1 = Persona("Aaron","Perez","53125743R")
cuenta1 = CuentaBancaria(persona1,300)

cuenta1.mostrar_info()
cuenta1.ingresar(500)
cuenta1.retirar(900)
cuenta1.mostrar_info()