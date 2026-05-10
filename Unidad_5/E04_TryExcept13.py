""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    FINALLY SIN EXCEPT

    Ejemplo: Liberar recursos de red (Ejemplo didactico solamnete)

    **) Con try-except-finally Tienes personal para atender emergencias 
        (except) y siempre cierras la puerta al salir (finally).
    **) Con try-finally (sin except) No tienes personal para emergencias, pero 
        igual siempre cierras la puerta pase lo que pase, incluso si hay un 
        terremoto o un incendio.

    Es como decir: No voy a resolver el problema, pero algo voy a hacer sí o 
    sí antes de que el programa termine (o explote).

    Sintaxis:

            try:
                # Código que puede fallar
            finally:
                # Esto se ejecuta SIEMPRE, haya error o no

    Importante: Si no pones except, el error no se captura, el programa se 
    detiene, pero antes de detenerse se ejecuta el finally.
"""
class abrir_conexion:
    def __init__(self):
        print('Conexión establecida')


def conectar_servidor():
    conexion = None
    try:
        conexion = abrir_conexion()  # Imaginemos que esta clase existe
        conexion.enviar_datos("Hola")
        # Aquí podría fallar la red
    finally:
        if conexion:
            conexion.cerrar()
            print("Conexión cerrada")
