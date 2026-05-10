""" TRACEBACK
    CÓMO CAPTURAR EL TRACEBACK COMO TEXTO (PARA REGISTROS O LOGS)

    Utilidad: 
    ---------
    Útil para aplicaciones donde quieres guardar el error completo en un 
    archivo de registro (log), pero mostrar un mensaje amigable al usuario.

    El traceback es mucho más útil para el programador porque te dice:
    -----------------------------------------------------------------

    *) ¿Qué archivo?
    *) ¿Qué línea?
    *) ¿Qué función?
    *) ¿Qué valores se estaban usando?

    
    Leer tracebacks como un experto
    -------------------------------

    Consejo	                        Explicación
    --------------------------------------------------------------------------
    No te asustes	        Los tracebacks largos son normales, solo mira la 
                            última línea primero
    Lee de abajo arriba	    El error real está al final, la causa está en las 
                            líneas superiores
    Busca tus archivos	    Ignora líneas de librerías internas de Python si 
                            son muchas
    Fíjate en los números	Te dicen la línea exacta del error
    El mensaje es clave	    Dice 'division by zero', 'list index out of range'
                            etc.
"""
import traceback

resultado = None

try:
    resultado =  10 / 0

except ZeroDivisionError:
    error_completo = traceback.format_exc()
    print("Guardando error en log:")
    print(error_completo)               # Ejecutar comentando esta linea
    # También podemos guardarlo en un archivo

