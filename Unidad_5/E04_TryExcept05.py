""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    USO DE EXCEPT SIN ESPECIFICAR TIPO (CAPTURA CUALQUIER EXCEPCIÓN).

    Cuándo sí usar except: sin tipo
   
    Situación	                            ¿Conviene?
    --------------------------------------------------------------------------
    Programas pequeños o scripts de	        Sí, es práctico
    una sola vez
    Registro de error genérico 	            Sí, si además guardas el error
    (guardar en un log)
    Cierre de recursos donde el error 	    Sí, con finally
    no es crítico
    Aplicaciones grandes o bibliotecas	    No, mejor errores específicos
    Cuando necesitas saber exactamente 	    No, usa tipos concretos
    qué falló

    Cómo capturar el error sin especificar tipo pero sin perder información
"""
try:
    resultado = 10 / 0

except Exception as e:      # Esto NO es exactamente sin tipo, pero casi
    print(f"Error genérico: {e}")
    print(f"Tipo del error: {type(e).__name__}")
