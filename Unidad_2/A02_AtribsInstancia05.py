""" Borrar un atributo de instancia usando DELATTR

    Alternativamente podemos usar delattr( funcion interconstruida de python)
    para borrar atributos de una instancia de una forma dinamica, basados
    en el valor de una variable

            delattr(instance, attribute)

    Recordar que no elimina la clase ni el objeto, solo los atributos de instancia
"""

class Player:
 
    def __init__(self, x, y, nombre, edad):
        self.x = x
        self.y = y
        self.nombre = nombre
        self.edad = edad


# Creamos una instancia
jugador01 = Player(6, 8, 'Roberto', 35)

# Definimos una lista de atributos (como cadenas)
mis_attributos = ['x', 'y']

# Ahora podemos iterar sobre esta lista de atributos y directamente
# borrarlos de la instancia jugador01
for attributo in mis_attributos:
    delattr(jugador01, attributo)

# Si revisamos los valores de estos atributos obtendremos error
# Esto debido a que ya no existen
# print(jugador01.x)
# print(jugador01.y)
print(jugador01.nombre)
print(jugador01.edad)
