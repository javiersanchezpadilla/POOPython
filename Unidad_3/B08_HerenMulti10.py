""" HERENCIA MULTIPLE:

    Puntos clave:
    -------------
    1)  Sintaxis: Nota que los padres se colocan dentro del paréntesis 
        separados por una coma: class Hija(Padre1, Padre2):.
    2)  Versatilidad: Permite crear objetos muy complejos combinando piezas 
        simples de funcionalidad.
    3)  El Orden Importa: Si ambos padres tienen un método llamado igual 
        (por ejemplo, __init__), Python usará el del primer padre que aparece 
        en la lista (de izquierda a derecha). Esto se llama MRO 
        (Method Resolution Order).

    Advertencia:
    ------------
    La herencia múltiple es como la sal en la comida: un poco es excelente, 
    mucha arruina el plato. Si abusan de ella, el código se vuelve muy difícil 
    de rastrear. En la práctica profesional, muchas veces se prefiere usar 
    'Composición', pero es vital que conozcan cómo funciona en Python.

    El Pato (Nadar y Volar)
    -----------------------
    En este ejemplo, usamos la herencia múltiple para combinar habilidades de 
    diferentes categorías.

    Este es un diagrama de esta jerarquía:

    Nadador  
            \
             \
              +------> Pato
             /
            /
    Volador

"""

class Nadador:
    def nadar(self):
        print("Nadando en el agua...")

class Volador:
    def volar(self):
        print("Volando por el aire...")

class Pato(Nadador, Volador):
    """Un pato puede hacer ambas acciones."""
    def graznar(self):
        print("¡Cuac, cuac!")

# El pato hereda de Nadador y de Volador
lucas = Pato()
lucas.nadar()
lucas.volar()
lucas.graznar()
