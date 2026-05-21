""" DECORADORES.

    El Decorador Más Simple del Mundo
    ---------------------------------
    Para crear un decorador básico, necesitamos una estructura de tres capas:

    1)  La función principal (el decorador).
    2)  Una función interna (la envoltura o wrapper) que ejecuta los extras.
    3)  El retorno de esa envoltura.

    Imaginemos que queremos un decorador que avise en consola justo antes y 
    justo después de que se ejecute cualquier función:
"""
                            # 1. Definimos el decorador
def mi_decorador(funcion_original):
    
                            # 2. Creamos la "funda" o envoltura
    def envoltura():
        print("[Antes] Se va a ejecutar la función...")
        
        funcion_original()  # Aquí se ejecuta el código de la función original
        
        print("[Después] La función ha terminado de ejecutarse.\n")
        
                            # 3. Devolvemos la envoltura armada
    return envoltura

# EL CÓDIGO CONTINUA EN EL SIGUIENTE PROGRAMA
