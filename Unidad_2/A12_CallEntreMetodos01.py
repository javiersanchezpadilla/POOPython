""" LLAMAR MÉTODOS DESDE OTROS MÉTODOS.

    Podemos llamar métodos desde otros métodos, de esta forma se puede reutilizar
    la funcionalidad que ya se implementó en la clase
    Si estamos llamando al Método “B” desde el Método “A”, la forma de llamarlo será

        self . method_b ( < arguments > )

    La diferencia con lo que se ha practicado hasta el momento es que se 
    reemplaza el nombre de la instancia por la palabra reservada self. En 
    la llamada (parámetros) no se escribe la palabra self como en la declaración
    de las funciones.

"""
class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item)     # Aqui mandamos a llamar al método add_item()

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Please provide a valid item")
    
my_backpack = Backpack()
print(my_backpack.items)
my_backpack.add_multiple_items(["Water Bottle", "Sleeping  Bag", "Candy", 123, "Pencil"])
print(my_backpack.items)

