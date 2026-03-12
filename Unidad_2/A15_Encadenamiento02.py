""" La Regla de Oro: "El objeto que regresa"

    El encadenamiento se rompe si uno de los métodos devuelve None 
    o un tipo de dato que no tiene el siguiente método.
    
    ¿Por qué falla? 
    ---------------
    Porque lista.sort() ordena la lista "in-place" (ahí mismo) y 
    devuelve None. Como None no tiene un método .append(), 
    el programa explota.
    """

# Esto fallará
lista = [3, 1, 2]
resultado = lista.sort().append(4)
