""" ORDEN PARA LLAMAR AL LOS MÉTODOS.

    MRO METHOD RESOLUTION ORDER
    2. Herencia Múltiple (Prioridad de Izquierda a Derecha)
    -------------------------------------------------------
    Cuando una clase hereda de dos padres al mismo tiempo, y ambos tienen el 
    mismo método, la prioridad la define el orden en que los escribiste dentro 
    de los paréntesis al declarar la clase.

    Resultado: Mensaje de la clase IZQUIERDA
    Como BaseIzquierda se colocó primero en la lista de herencia 
    (BaseIzquierda, BaseDerecha), Python le otorga prioridad absoluta sobre 
    la de la derecha.
"""
class BaseDerecha:
    def mensaje(self):
        print("Mensaje de la clase DERECHA")

class BaseIzquierda:
    def mensaje(self):
        print("Mensaje de la clase IZQUIERDA")

# El orden en los paréntesis es fundamental
class Hija(BaseIzquierda, BaseDerecha):
    # La clase Hija está vacía
    pass

# Prueba
print("\n--- Ejemplo Múltiple ---")
objeto_hija = Hija()
objeto_hija.mensaje()

# Obteniendo el MRO Method Resolution Orden (ambas maneras son válidas)
print(Hija.mro())
print(Hija.__mro__)

