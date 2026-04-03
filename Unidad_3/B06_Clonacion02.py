""" CORRECCIÓN AL ERROR DEL PROGRAMA B05_Inmutabil03.py

    Ejemplo del riesgo de mutabildiad con un diccionario
    En este ejemplo se esperaba que al recorrer el diccionario se eliminaran
    los elementos cuyo valor sea par, pero eso causa un error de ejecución

        RuntimeError: dictionary changed size during iteration

    y es que al eliminar un elemento del diccinario se modifica el tamaño 
    del mismo originalmente el tamaño es 4 y va bajando.

    SOLUCIÓN.
    ---------
    Clonar el diccionario

"""


def elimina_valores_pares(diccionario):
    # ciclamos con la copia clonada del diccionario
    for llave, valor in diccionario.copy().items(): 
        if valor % 2 == 0:
            del diccionario[llave]  # afectamos el dicc original


mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(mi_diccionario)           # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
elimina_valores_pares(mi_diccionario)
print(mi_diccionario)           # {'a': 1, 'c': 3}
