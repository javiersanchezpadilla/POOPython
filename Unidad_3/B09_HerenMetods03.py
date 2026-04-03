"""


"""

class CuentaBancaria:
 
    def __init__(self, propietario, balance, divisa):
        self.propietario = propietario
        self.balance = balance
        self.divisa = divisa
 
    def imprime_balance(self):
        print("Su valance actual es:")
        print(self.balance) 
 
    def hacer_deposito(self, monto):
        if monto > 0:
            self.balance += monto
        else:
            print("Introduzca un monto valido.")
 
    def retirar_dinero(self, monto):
        if self.balance - monto >= 0:
            self.balance -= monto
        else:
            print("No tienes suficientes fondos para hacer el retiro.")
 
 
class CuentasDeAhorro(CuentaBancaria):
 
    TASA_DE_INTERES = 0.035
 
    def __init__(self, propietario, balance, divisa):
        CuentaBancaria.__init__(self, propietario, balance, divisa)
        self.tasa_de_interes = CuentasDeAhorro.TASA_DE_INTERES
 
    def intereses_ganados(self):
        interes_ganado = self.balance * CuentasDeAhorro.TASA_DE_INTERES
        self.balance += interes_ganado
 
 
class VerificaCuentaBancaria(CuentaBancaria):
 
    def __init__(self, propietario, balance, divisa, tarjeta_debito=None, tarjeta_credito=None):
        CuentaBancaria.__init__(self, propietario, balance, divisa)
        self.tarjeta_debito = tarjeta_debito
        self.tarjeta_credito = tarjeta_credito
 
 
mi_cuenta_de_ahorro = CuentasDeAhorro("Nora Nav", 45600, "USD")
 
mi_cuenta_de_ahorro.imprime_balance()
mi_cuenta_de_ahorro.hacer_deposito(5000)
mi_cuenta_de_ahorro.retirar_dinero(200)
 
mi_cuenta_de_ahorro.intereses_ganados()
mi_cuenta_de_ahorro.imprime_balance()
 
my_checking_account = VerificaCuentaBancaria("Nora Nav", 67899, "GBP")
 
my_checking_account.imprime_balance()
my_checking_account.hacer_deposito(4000)
my_checking_account.retirar_dinero(100)
