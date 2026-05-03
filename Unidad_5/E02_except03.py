""" MANEJO DE EXCEPCIONES USANDO CLASES

    Cajero Automático
    -----------------
    Manejamos la validación de la tarjeta y luego la transacción del saldo.
"""
class CajeroTokens:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def retirar_token(self):
                                                # Validación de identidad
        try:
            nip = input("Ingrese su NIP: ")
            if not nip.isdigit():
                raise TypeError("El NIP solo debe contener números.")
        except TypeError as e:
            print(f"Error de identidad: {e}")
            return

                                                # Transacción
        try:
            costo = 10
            if self.saldo < costo:
                raise RuntimeError("Saldo insuficiente.")
            self.saldo -= costo
            print(f"Token generado. Saldo restante: {self.saldo}")
        except RuntimeError as e:
            print(f"Error de cuenta: {e}")


cajero = CajeroTokens(5) # Saldo bajo para forzar el segundo bloque
cajero.retirar_token()
