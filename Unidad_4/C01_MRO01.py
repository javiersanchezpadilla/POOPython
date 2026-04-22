""" ORDEN PARA LLAMAR AL LOS MÉTODOS.

    MRO METHOD RESOLUTION ORDER
    Esta es una de las dudas más comunes y, a la vez, más importantes para 
    entender el MRO (Method Resolution Order) o el Orden de Resolución de 
    Métodos en Python.

    Python es 'perezoso': en cuanto encuentra el método que busca siguiendo su 
    camino lógico, se detiene y lo ejecuta, ignorando los demás.

    1. Herencia Multinivel (Prioridad por Cercanía)
    -----------------------------------------------
    En una jerarquía de niveles (Abuelo → Padre → Hijo), si el Hijo no tiene el 
    método, Python buscará en el ancestro más cercano (el Padre). Solo si el 
    Padre no lo tiene, subirá hasta el Abuelo.

    Resultado: ¡Hola desde el Padre!
    Aunque el Abuelo tiene el método, el Padre está 'más cerca' en la línea 
    sucesoria. Python encuentra el método en el nivel inmediato superior y 
    deja de buscar.
"""
class Abuelo:
    def saludar(self):
        print("¡Hola desde el Abuelo!")

class Padre(Abuelo):
    def saludar(self):
        print("¡Hola desde el Padre!")

class Hijo(Padre):
    # La clase Hijo está vacía, no tiene el método 'saludar'
    pass
    # def saludar(self):
    #     print("¡Hola desde el hijo!")

# Prueba
print("--- Ejemplo Multinivel ---")
objeto_hijo = Hijo()
objeto_hijo.saludar()

# Obteniendo el MRO Method Resolution Orden (ambas maneras son válidas)
print(Hijo.mro())
print(Hijo.__mro__)
