""" Concatenación de Inventarios (__add__)

    Este es un ejemplo clásico de videojuegos o sistemas de logística. 
    Si tienes dos "mochilas" de ítems, ¿qué pasa si las unes?
"""
class Inventario:
    def __init__(self, items):
        self.items = items # Esperamos una lista

    # Sobrecarga de +
    def __add__(self, otro):
        # Unimos las dos listas y devolvemos un nuevo objeto Inventario
        nueva_lista = self.items + otro.items
        return Inventario(nueva_lista)

    def __str__(self):
        return f"Inventario actual: {', '.join(self.items)}"

# Uso
mochila_p1 = Inventario(["Espada", "Escudo"])
mochila_p2 = Inventario(["Poción", "Cuerda"])

gran_mochila = mochila_p1 + mochila_p2
print(gran_mochila) # Resultado: Inventario actual: Espada, Escudo, Poción, Cuerda
