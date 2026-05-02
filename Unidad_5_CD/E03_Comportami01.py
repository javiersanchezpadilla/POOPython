""" PATRONES DE DISEÑO (DE COMPORTAMIENTO)

    5. Patrones de Comportamiento: Ejemplo - Strategy (Estrategia)
    --------------------------------------------------------------
    El patrón Strategy permite definir una familia de algoritmos, poner cada 
    uno en una clase separada y hacer que sus objetos sean intercambiables.

    Ejemplo: Un sistema de pagos. El cliente puede elegir pagar con PayPal, 
    Tarjeta de Crédito o Criptomonedas. El 'Contexto' (el carrito) no cambia, 
    solo cambia la 'Estrategia' de pago.

    Por qué enseñar esto después del Polimorfismo
    ---------------------------------------------
    Si observamos el código, el patrón Strategy es puro polimorfismo en acción
    Enseñar patrones es la mejor forma de entender para qué sirve todo lo que 
    hemos aprendido antes (interfaces, herencia, clases abstractas).

"""
from abc import ABC, abstractmethod

# Interfaz Estrategia
class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass

# Estrategias concretas
class PagoTarjeta(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando {monto} usando Tarjeta de Crédito.")

class PagoPayPal(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando {monto} usando PayPal.")

# Contexto (El Carrito de compras)
class Carrito:
    def __init__(self, estrategia_pago: MetodoPago):
        self.estrategia = estrategia_pago

    def procesar(self, total):
        self.estrategia.pagar(total)

# Prueba
mi_compra = Carrito(PagoPayPal())
mi_compra.procesar(500)

# Podemos cambiar la estrategia dinámicamente
mi_compra.estrategia = PagoTarjeta()
mi_compra.procesar(500)
