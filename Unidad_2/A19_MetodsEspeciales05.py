""" MÉTODO __len__( )

    object.__len__(self)
    Se llama para implementar la función incorporada len(). Debería devolver 
    la longitud del objeto, un número entero >= 0. Además, un objeto que no 
    define un método _bool_() y cuyo método _len_() devuelve cero se considera 
    falso en un contexto booleano.

    Detalle de la implementación de CPython: en Python, se requiere que la 
    longitud sea como máximo sys.maxsize. Si la longitud es mayor que sys.maxsize, 
    algunas funciones (como len()) pueden generar OverflowError. Para evitar generar 
    OverflowError mediante pruebas de valor de verdad, un objeto debe definir 
    un método _bool_( ).
"""
mi_cadena = "Hola mundo!!!"
print('La longitud de mi cadena', len(mi_cadena))
print('La longitud de mi cadena', mi_cadena.__len__())

mi_lista = [1, 2, 3 ,4, 5]
print('\nLa longitud de mi lista', len(mi_lista))
print('La longitud de mi lista', mi_lista.__len__())

mi_tupla = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
print('\nLa longitud de mi tupla', len(mi_tupla))
print('La longitud de mi tupla', mi_tupla.__len__())

mi_diccionario = {"a":1, "b":2, "c":3, "d":4}
print('\nLa longitud de mi diccionario', len(mi_diccionario))
print('La longitud de mi diccionario', mi_diccionario.__len__())

mi_conjunto = {1, 1, 1, 2, 3, 4, 2, 2, 2, 3, 4, 5, 1, 1, 1, 1}
print('\nTrabjaremos con los conjuntos')
print(mi_conjunto)
print('La longitud de mi conjunto', len(mi_conjunto))
print('La longitud de mi conjnuto', mi_conjunto.__len__())

# Para el ejemplo de la mochila
class Mochila:

    def __init__(self):
        self.articulos = []

    def agregar_articulos(self, articulo):
        self.articulos.append(articulo)

    def elimina_articulo(self, articulo):
        if articulo in self.articulos:
            self.articulos.remove(articulo)
        else:
            print("Este articulo no existe en la mochila")

    def __len__(self):
        return len(self.articulos)
    
mi_mochila = Mochila()
mi_mochila.agregar_articulos("Botella de agua")
mi_mochila.agregar_articulos("Chocolate")
mi_mochila.agregar_articulos("cuaderno")

print(len(mi_mochila))
