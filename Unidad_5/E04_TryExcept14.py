""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    ¿QUÉ PASA SI HAY UN RETURN DENTRO DEL TRY?

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
"""
def ejemplo():
    try:
        return "Hola"
    
    finally:
        print("Esto se ejecuta ANTES del return")
    print("Esto nunca se ejecuta")


resultado = ejemplo()
print(resultado)
