""" Definición de otro ejemplo para el uso de métodos

    Ahora veamos algunas pautas para escribir nombres de métodos en Python:

    **) Directriz 1. Los nombres de los métodos deben seguir la convención 
        de nomenclatura de snake_case. Deben escribirse en minúsculas y las palabras 
        deben estar separadas por guiones bajos.
        Ejemplo: display_data   mostrar_datos

    **) Directriz 2. Los nombres de los métodos deben contener verbos ya que 
        representan acciones.
        Ejemplo: find_area      encontrar_Area

    **) Directriz 3. Si el método devuelve un valor booleano (Verdadero o Falso), 
        su nombre debe describirlo.
        Estos nombres suelen empezar con is o has, u otro prefijo que indique que 
        su valor de retorno será un valor booleano.
        Ejemplos is_red, has_children   es_rojo, tiene_hijos
"""

class Backpack:

    def __init__(self):
        self._item = []

    @property
    def items(self):
        return self._items
    
    def add_item(self, item):
        if isinstance(item, str):
            self._item.append(item)
        else:
            print('Please provide a valid item')

    def remove_item(self, item):
        if item in self._item:
            self._items.remove(item)
            return 1
        else:
            return 0
        
    def has_item(self, item):
        # Regresa verdadero o falso si está o no
        return item in self._items: 
