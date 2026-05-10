""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    ERROR COMÚN: PENSAR QUE FINALLY CAPTURA ERRORES

    Sorpresa: El bloque finally se ejecuta antes de que el return devuelva el 
    valor. Es como si Python dijera: 
    Veo un return, pero primero déjame ejecutar el finally.


    Cuándo usar try-finally sin except
    ----------------------------------
    Situación	                       ¿Recomendado?	   Ejemplo
    --------------------------------------------------------------------------
    Cerrar archivos	                        Sí	        archivo.close()
    Cerrar conexiones a BD	                Sí	        conexion.close()
    Liberar memoria externa	                Sí	        liberar_recurso()
    Registrar logs de errores	            Parcial	    Mejor con except
    Evitar que el programa termine	        No	        Usa except
    Mostrar mensajes amigables al usuario   No	        Usa except

    Reumen:
    -------

    Con except:

        try --> except (si hay error, lo capturo y sigo) --> finally (siempre)

    Sin except:
        try --> finally (siempre, pero el error NO se captura y el programa se 
                detiene después)

"""

try:
    x = 10 / 0

        # El programa se detiene después del finally. 
        # finally no captura el error, solo asegura que algo se ejecute 
        # antes de que el programa caiga.
finally:
    print("Limpiando...")

print("Esto nunca se ejecuta")          # El error detiene el programa
