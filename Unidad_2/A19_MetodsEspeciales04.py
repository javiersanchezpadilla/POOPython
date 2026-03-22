""" Método __repr__()

    Los métodos especiales __str__( )  y  __repr__( ) pueden parecer similares 
    a primera vista cuando leemos la documentación porque ambos retorna una 
    cadena que describe un objeto, sin embargo son muy diferentes entre sí.

    __str__( )
    ==========
    1)  Proporciona una representación informal del objeto destinado a los 
        usuarios finales.
    2)  Favorece la legibilidad sobre los detalles o la precisión.
    3)  Llamado por las funciones integradas str(), format() y print().

    Este método difiere de object.__repr__( ) en que no se espera que __str__( ) 
    devuelva una expresión Python válida: se puede utilizar una representación 
    más conveniente o concisa.

    __repr__( )
    ===========
    1)  Proporciona una representación formal del objeto destinado a los 
        desarrolladores.
    2)  Esta representación se utiliza para la depuración.
    3)  Llamado por la función incorporada repr().

    Si es posible, esto debería verse como una expresión Python válida que podría 
    usarse para recrear un objeto con el mismo valor (dado un entorno apropiado). 
    Si esto no es posible, se debe devolver una cadena del formato 
    <...alguna descripción útil...>.
"""
class Playera:
    def __init__(self, color, tamanio, marca):
        self.color = color
        self.tamanio = tamanio
        self.marca = marca
 
    def __str__(self):
        return f"Color: {self.color}; Tamaño: {self.tamanio}; Marca: {self.marca}"
  
    # lo que regreamos es una expresion, entonces podemos formar la siguiente 
    # expresión para posteriormete declarar otro objeto
    # Playera('Azul', 'EG', 'Retro Land'), la cual podrá ser evaluada posteriormente
    # mediante el uso de eval(<expresion>)

    def __repr__(self):
        return f'Playera ("{self.color}", "{self.tamanio}", "{self.marca}")'
 
mi_playera = Playera("Azul", "EG", "Retro Land")
 
print("__str__() -", str(mi_playera))
 
print("\n__repr__() -", repr(mi_playera))
 
    # Aqui es donde recreamos otro objeto mediante eval(expresion>), esto es,
    # a diferencia de __str__ aquí tendremos una expresión validida que podrá
    # ser evaluada mediante eval, lo que estaremos evaluando es
    # mi_otra_playera = eval(Playera('Azul', 'EG', 'Retro Land'))
mi_otra_playera = eval(repr(mi_playera))
 
print("\n(Nuevo Objeto)", mi_otra_playera)

# Como funciona eval()
print(eval('1+3+4'))
