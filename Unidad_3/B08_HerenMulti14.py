""" HERENCIA MULTIPLE.

    Herencia Múltiple con __init__
    ------------------------------
    Este es el caso más real. ¿Cómo inicializamos los datos de dos padres 
    distintos usando super()?

    Puntos clave:
    -------------
    1)  Prioridad de Izquierda a Derecha: El orden en los paréntesis define 
        quién gana en caso de empate.
    2)  Uso de __mro__: usar 

            print(Jugador.__mro__) 

        en la consola. Python les mostrará exactamente el camino que sigue 
        para buscar cualquier método.
    3)  Llamada Explícita: Cuando hay varios padres con parámetros muy 
        diferentes en sus __init__, a veces es mejor llamar a 

            ClasePadre.__init__(self, ...) 

        directamente en lugar de usar super(), para evitar confusiones en el 
        paso de argumentos.

    Reflexión:
    ----------
    La herencia múltiple es potente pero peligrosa. Un buen diseño de software 
    intenta evitarla usando Composición (un objeto tiene otros objetos) en 
    lugar de herencia múltiple (un objeto es muchas cosas a la vez).
"""

class Identidad:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Identidad creada: {self.nombre}")

class SistemaSalud:
    def __init__(self, puntos_vida):
        self.puntos_vida = puntos_vida
        print(f"Sistema de salud: {self.puntos_vida} HP")

class Jugador(Identidad, SistemaSalud):
    def __init__(self, nombre, puntos_vida, nivel):
        # En herencia múltiple compleja, a veces es más claro
        # llamar a los padres por su nombre de clase:
        Identidad.__init__(self, nombre)
        SistemaSalud.__init__(self, puntos_vida)
        self.nivel = nivel
        print(f"Jugador de nivel {self.nivel} inicializado.")

# Creación del objeto
prota = Jugador("Javier", 100, 1)
print(Jugador.__mro__)  # Muestra el orden de resolución de métodos (MRO)
