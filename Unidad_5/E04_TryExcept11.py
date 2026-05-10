""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    FINALLY SIN EXCEPT

    Imagina que eres el encargado de un cine:

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

    # ¿Como funciona el programa?
    # Si todo sale bien --> escribe, cierra el archivo.
    # Si hay un error (ejemplo: disco lleno) --> el programa se detiene 
    # mostrando el error, pero igual cierra el archivo antes de detenerse.

try:
    archivo = open("datos.txt", "w")
    archivo.write("Hola mundo")
    # Aquí podría ocurrir un error (disco lleno, sin permisos, etc.)

finally:
    archivo.close()  # Esto se ejecuta SIEMPRE
    print("Archivo cerrado (aunque haya error)")
