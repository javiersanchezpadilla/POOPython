""" En Pytyon todo es un ojeto

    OBJECT Es la clase base de la cual heredan todas las clases en Python
    En Python, todas las clases que creas heredan de object de forma automática
    incluso si no lo escribes explícitamente.

    1. El Concepto de 'Todo es un Objeto'
    -------------------------------------
    Cuando decimos que en Python 'todo es un objeto', nos referimos a que 
    incluso los tipos de datos más básicos (como números o cadenas) tienen a 
    <object> en la cima de su árbol genealógico.

    **) Un entero (int) es un objeto.
    **) Una cadena (str) es un objeto.
    **) Una función es un objeto.
    **) Incluso una clase es un objeto.

    2. ¿Qué hereda una clase de <object>?
    -------------------------------------
    Al heredar de esta clase base, tus objetos obtienen comportamientos 
    esenciales (métodos especiales) que Python necesita para gestionarlos. 
    Algunos de estos 'métodos mágicos' (Dunder methods) son:

    1)  __init__: Para inicializar el objeto.
    2)  __str__: Para definir cómo se ve el objeto cuando lo imprimes con print().
    3)  __repr__: Para la representación interna del objeto.
    4)  __eq__: Para poder comparar dos objetos con el operador ==.

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
