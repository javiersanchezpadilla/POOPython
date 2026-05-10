""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    FINALLY SIN EXCEPT

    Tabla Comparativa: try-finally contra try-except-finally
    --------------------------------------------------------

    Característica	        try-finally	                try-except-finally
    ---------------------------------------------------------------------------
    Captura el error	          No	                    Sí
    El programa se detiene	      Sí (muestra el error)	    No (si hay except)
    Se ejecuta finally	          Siempre	                Siempre
    Útil para limpiar recursos	  Mucho	                    También
    Útil para evitar que el 	  No	                    Sí
    programa termine

    Ejemplo: Contador de intentos (sin capturar error)
    El finally se ejecutará (incrementará el contador a 2), pero después el 
    programa mostrará el error y se detendra.
"""
intentos = 0
try:
    intentos += 1
    resultado = 10 / 0  # Esto falla
    print("Esto no se imprime")

finally:
    intentos += 1
    print(f"Se hicieron {intentos} intento(s) antes del error")

    # El programa muestra el error y se detiene después del finally
