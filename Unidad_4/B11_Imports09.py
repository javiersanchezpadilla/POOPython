""" EL CONCEPTO DE __ALL__

    La lista __all__ es una variable global que defines en tu archivo de 
    módulo (.py). Esta lista contiene los nombres de las funciones, clases 
    y variables que deseas exponer y que deben ser visibles cuando se usa 
    la sintaxis de importación con asterisco (*).

    Pensemos que este es un módulo para que otros programas lo importen
"""
def funcion_publica_1():
    """Esta queremos que se pueda importar."""
    print("Función pública 1 ejecutada.")

def funcion_privada_auxiliar():
    """Esta NO queremos que se importe con el asterisco."""
    print("Función privada auxiliar ejecutada.")

class ClaseVisible:
    """Clase que debe ser accesible."""
    pass

mi_variable_publica = "Hola desde mi variable"
mi_variable_protegida = "Top secret"

        # **CLAVE:** Definición de __all__
        # Solo incluimos los nombres que queremos exponer.
__all__ = [ "funcion_publica_1", "ClaseVisible", "mi_variable_publica" ]

