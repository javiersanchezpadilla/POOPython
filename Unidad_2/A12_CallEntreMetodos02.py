""" Esta es una de las prácticas más importantes en la programación, ya que 
    permite que tus clases sean ordenadas y que no tengas que repetir el 
    mismo código una y otra vez. A esto le llamamos reutilización de código 
    interna.

    En Python, para que un método llame a otro dentro de la misma clase, es 
    indispensable usar la palabra clave self. antes del nombre del método.

            self.<nombre_del_metodo()>

    1. El método "Validador" (Nivel Seguridad)
    En este ejemplo, un método principal (depositar) llama a un método de apoyo 
    (__validar_monto) para verificar que el dinero sea real antes de sumarlo 
    al saldo.

    Puntos clave:
    -------------
    **) El puente self: Sin el self., Python buscará una función fuera de la clase 
        y lanzará un error porque no encontrará el método.
    **) Modularidad: Es mejor tener 5 métodos pequeños que hacen una sola cosa bien, 
        que un método gigante que hace todo.
    **) Privacidad: Nota que en los ejemplos 1 y 3 usé el doble guion bajo (__). 
        Esto es porque esos métodos son "ayudantes" y no queremos que el usuario los 
        llame desde afuera; solo la clase debe usarlos.
"""

class Cajero:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def __validar_monto(self, monto):
        """Método privado de apoyo para validación."""
        return isinstance(monto, (int, float)) and monto > 0

    def depositar(self, cantidad):
        """Método principal que llama al validador."""
        if self.__validar_monto(cantidad):      # <-- Llamada interna
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Error: El monto no es válido.")


atm = Cajero(100)
atm.depositar(50)
