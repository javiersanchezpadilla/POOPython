""" RAISE

    raise TypeError (mensaje)

    
    Es como tocar la alarma de incendios sin decir por qué. Suena la alarma, 
    pero nadie sabe si es fuego, humo o una prueba. Es mejor dar el mensaje 
    específico.

    ¿Cuándo usarlo?
    ---------------

    *)  Rara vez. Casi siempre es mejor incluir un mensaje
    *)  Solo cuando el tipo de error ya es suficientemente descriptivo
    *)  En código muy simple o prototipos rápidos
"""
def sumar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                     # Lanza el error con mensaje por defecto
        raise TypeError ("Ambos argumentos deben ser números")    
    return a + b

# Probamos
try:
    sumar("hola", 5)
except TypeError as e:
    print(f"Error: {e}")
