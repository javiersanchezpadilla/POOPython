""" MANEJO DE EXCEPCIONES.

    Creación de Excepciones Personalizadas
    --------------------------------------
    Para proyectos grandes, es mejor crear nuestras propias excepciones 
    heredando de la clase Exception. Esto da mucha claridad al código.

    Consejos y recomendaciones:
    ---------------------------
    1)  No usar el except vacío: Poner solo except: (sin especificar el tipo
        de error) es una mala práctica, porque oculta errores que sí 
        deberíamos ver (como errores de sintaxis).
    2)  Principio EAFP: En Python se usa el lema "It's easier to ask for 
        forgiveness than permission" (Es más fácil pedir perdón que pedir 
        permiso). En lugar de poner mil if para revisar si todo está bien, 
        es preferible intentar la operación en un try y manejar la excepción 
        si algo falla.
"""
class ErrorConexionServidor(Exception):
    """Excepción para cuando falla la red del campus"""
    pass

def conectar_a_base_de_datos():
    internet = False
    if not internet:
        raise ErrorConexionServidor("No hay conexión con el servidor del ITA.")

try:
    conectar_a_base_de_datos()
except ErrorConexionServidor as e:
    print(f"Aviso al usuario: {e}")
