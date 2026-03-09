"""SINTAXIS ALTERNATIVA PARA LLAMAR UN MÉTODO.

    Ya sabemos cómo llamar a un método en una instancia usando notación de 
    puntos. Esta es la forma más común de llamar a un método en Python.

    Sin embargo, también tenemos otra alternativa por si la encuentras en 
    proyectos reales.

    Sintaxis alternativa

            <ClassName>.<method>(<instance>, <arguments>)

    De izquierda a derecha encontramos:

    El nombre de la clase.
    Un punto.
    El nombre del método.
    Entre paréntesis, la instancia (como primer argumento) seguida de los argumentos 
    del método separados por comas.

    El valor para self?
    -------------------
    Note que ahora si estamos pasando un valor para  self.
    Es el primer argumento: la instancia.

    Por ejemplo:

            Backpack.add_item(my_backpack, "Water")

    En este ejemplo llamamos a los metodos referenciando la clase y enviando 
    como argumento el nombre de la instancia, este ejemplo es el mismo del 
    código anterior.
"""

class Mochila:

    def __init__(self):
        self._articulos = []

    @property
    def articulos(self):
        return self._articulos
    
    def agregar_articulos(self, articulo):
        if isinstance(articulo, str):
            self._articulos.append(articulo)
        else:
            print("Por favor provee un articulo valido")
    
    def elimina_articulo(self, articulo):
        if articulo in self._articulos:
            self._articulos.remove(articulo)
            return 1
        else:
            print("Este articulo no se encuentra en la mochila")
            return 0
        
    def tiene_el_articulo(self, articulo):
        return articulo in self._articulos
    

mi_mochila = Mochila()
print(mi_mochila.articulos)

# Agregamos una botella de agua a la mochila
Mochila.agregar_articulos(mi_mochila, "Botella de Agua")
print(mi_mochila.articulos)

# Agregamos una bolsa de dormir
Mochila.agregar_articulos(mi_mochila, "Bolsa de dormir")
print(mi_mochila.articulos)

# Verificamos si tenemos una botella de agua en la mochila
tiene_agua = Mochila.tiene_el_articulo(mi_mochila, "Botella de Agua")
print(tiene_agua)

# Sacamos de la mochila la botella de agua
Mochila.elimina_articulo(mi_mochila, "Botella de Agua")
print(mi_mochila.articulos)

# Sacamos de la mochila la bolda de dormir
Mochila.elimina_articulo(mi_mochila, "Bolsa de dormir")
print(mi_mochila.articulos)

# Intentamos eliminar algo que no esta en la mochila
Mochila.elimina_articulo(mi_mochila, "Dulce")
print(mi_mochila.articulos)
