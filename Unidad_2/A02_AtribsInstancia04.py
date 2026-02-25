""" Borrar atributos de instancia con DEL

    Para borrar un atributo de instancia especifico, podemo usar la
    funcion 'del'

        del nombre_instancia.atributo_de_instancia
"""

class Perro:
 
    def __init__(self, nombre, color, edad):
       self.nombre = nombre
       self.color = color
       self.edad = edad


# Creamos una instancia
perro = Perro("Firulais", 'Negro', 5)

# Antes de borrar verificamos los atributos de la instancia
print(perro.nombre)
print(perro.color)
print(perro.edad)

# Como vemos tiene todos sus atributos
# Ahora borramos el atributo edad
print('\n Nuevos valores')
del perro.edad
print(perro.nombre)
print(perro.color)

# AttributeError: 'Perro' object has no attribute 'nombre'
# print(perro.edad)
