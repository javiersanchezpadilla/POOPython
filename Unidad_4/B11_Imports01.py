""" DECLARACIÓN DE IMPORTACIONES

    DECLARACIÓN DE IMPORTACIÓN          PARA ACCEDER AL ELEMENTO
    --------------------------------    ------------------------
    import <módulo>                     <módulo>.<elemento>
    from <módulo> import <elemento>     <elemento>
    from <módulo> import *              <elemento>
    import <módulo> as <etiqueta>       <etiqueta>.<elemento>

    EJEMPLO DE IMPLEMENTACIÓN.
    import mi_modulo                    mi_modulo.foo()
    from mi_modulo import foo()         foo()
    from mi_modulo import *             foo()
    import mi_modulo as modulo_alias    modulo_alias.foo()

    Cuando escribimos código en un fichero con extensión .py, realmente 
    estamos creando un módulo. Si luego creamos otro fichero para escribir
    código nuevo, podemos reutilizar el código que ya hemos usado, importándolo
    como un módulo. También podemos importar módulos que ofrece python, 
    ahorrando tiempo y esfuerzo.

    El siguiente código actuará como un módulo, el cual importatemos desde 
    el programa B11_imports02.py
"""

variable = "Variable de mi módulo"

def mi_funcion():
    print("Hola desde mi función")

class MiClase:
    def __init__(self):
        print("Hola desde mi clase")

if __name__ == '__main__':
    print(variable)
    mi_funcion()
    a = MiClase()
    print(__file__)     # Ruta del archivo 
