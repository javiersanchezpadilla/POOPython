""" TRACEBACK

    EN LOS SIGUIENTES EJEMPLOS SE COMETERAN ERRORES PARA PODER EXPLICAR 
    EL CONCEPTO DE TRACEBACK

    Error común con listas
    Así queda el traceback
    Traceback (most recent call last):
    File "/home/javier/...../E05_traceback03.py", line 19, in <module>
    procesar()
    File "/home/javier/...../E05_traceback03.py", line 15, in procesar
    valor = obtener_valor(datos, 10)
            ^^^^^^^^^^^^^^^^^^^^^^^^
    File "/home/javier/...../E05_traceback03.py", line 11, in obtener_valor
    return lista[indice]
           ~~~~~^^^^^^^^
    IndexError: list index out of range

    
    Lo que nos dice este traceback:
    -------------------------------
    
    **) El error es IndexError (índice fuera de rango)
    **) Ocurrió en obtener_valor (línea 11)
    **) La función procesar llamó a obtener_valor con el índice 10
    **) La lista solo tiene 3 elementos (índices 0, 1, 2)

    Tipos de traceback según el error
    ----------------------------------
    
    Error	                    ¿Qué verás en el traceback?
    --------------------------------------------------------------------------
    ZeroDivisionError   La línea con a / b donde b es cero
    IndexError	        La línea con lista[indice] donde indice es muy grande
    KeyError	        La línea con diccionario[clave] donde clave no existe
    ValueError	        La línea con int(texto) donde texto no es número
    FileNotFoundError	La línea con open(archivo) donde archivo no existe
"""
def obtener_valor(lista, indice):
    return lista[indice]

def procesar():
    datos = [1, 2, 3]
    valor = obtener_valor(datos, 10)
    print(valor)


procesar()
