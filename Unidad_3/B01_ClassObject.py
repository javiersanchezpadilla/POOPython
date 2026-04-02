""" En Pytyon todo es un ojeto

    OBJECT Es la clase base de la cual heredan todas las clases en Python

"""

print(object)

# Comprobaremos si todos los valores que hemos estado usando hasta
# ahora son instancias de esta clase
print('Un valor entero:', isinstance(5, object))
print('Una cadena', isinstance("Hola mundo", object))
print("Una lista", isinstance([1, 2, 3, 4, 5], object))
print("Un diccionario", isinstance({'a':1, 'b':2, 'c':3}, object))
print("Un conjunnto", isinstance({1, 2, 3, 4}, object))
print("Un booleano", isinstance(True, object))

def mi_funcion(x):
    return x ** 2

print(mi_funcion(10))
print("En una funcion", isinstance(mi_funcion, object))

class Pelicula:
    def __init__(self, nombre):
        self.nombre = nombre

print("En una clase", isinstance(Pelicula, object))
print("LA clase entero", isinstance(int, object))
