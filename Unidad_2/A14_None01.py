""" VALOR NONE.

    None es uno de los conceptos más importantes y, a veces, más incomprendidos 
    por quienes vienen de otros lenguajes.

    En términos sencillos: None es un objeto especial de Python que se utiliza 
    para representar la <ausencia de valor> o el <vacío>.

    Aquí tienes los puntos clave para explicarlo:

    1. No es Cero, no es Falso, no es un String Vacío
    -------------------------------------------------
    Es vital entender que None es su propio tipo de dato (NoneType).

    A)  No es 0: El cero es un número (tiene valor matemático).
    B)  No es False: Aunque en un if se comporta como falso, no es un valor 
        booleano.
    C)  No es "": Un string vacío es un texto que simplemente no tiene letras.

    None es <'aquí no hay nada'>.

    2. Uso como "Marcador de Posición" (Placeholder)
    ------------------------------------------------
    Como vimos en los ejercicios de sobrecarga y setters, usamos None para decir: 
    "Este dato todavía no existe o no se ha proporcionado".

"""
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.telefono = None  # El usuario aún no ha dado su teléfono

