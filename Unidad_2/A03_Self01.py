""" PROPÓSITO DE SELF.

    Self, es una forma genérica de referirse a la instancia actual de la clase
    la instancia que se está creando en el caso de __init__ o la instancia que
    es como llamar o ejecutar una acción en el caso de los métodos. 
    Realmente self se refiere a los atributos de la instancia u objeto, esto 
    permite diferenciar unos atributos de otros en cada objeto

    De la instanicia            Al atributo de
    que esta siendo --+     +-- instancia precio
    creada            |     | 
                      v     v                   Asigna el valor de la 
                     self.precio = precio   <-- variable precio

    Es muy importante entender que 'self.precio' no es lo mismo que 'precio' 
    son totalmente independientes, 'self.precio'  es el atributo de la instancia 
    o de objetos concretos, mientras que 'price' es el valor que estamos asignando
    al momento de crear la instancia mediante la clase.

    Es muy importante saber que estos dos elementos no son iguales, son 
    completamente independientes, este es el parámetro que definimos en el método 
    init, es como cualquier otro parámetro, como los parámetros que definimos en 
    cualquier función regular que escribimos y esto de aquí es el atributo de la 
    instancia.

    Ejemplo de creación de una clase
"""

class Mochila:

    def __init__(self, color, tamanio):
        self.articulos = []
        self.color = color
        self.tamanio = tamanio 


mi_mochila = Mochila('Rojo', 'grande')    
print(mi_mochila.color)
print(mi_mochila.tamanio)

mi_mochila.articulos.extend(['Vaso', 'Lapiz', 'Pluma', 'Botella'])
print(mi_mochila.articulos)
