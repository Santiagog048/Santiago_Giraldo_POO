class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            return True
        else:
            return False
    
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.balance:
            self.balance -= cantidad
            return True
        else:
            return False
    
    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
    
    def mostrar_detalles(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", ', '.join(self.propietarios))
        print("Balance:", self.balance)

cuenta = CuentaBancaria('123456789', ['Juan', 'María'], 1500.00)

cuenta.depositar(500)
cuenta.retirar(200)
cuenta.aplicar_cuota_manejo()

cuenta.mostrar_detalles()