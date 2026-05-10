""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    CAPTURAR EL ERROR ESPECIFICO SIN MOSTRAR EL MENSAJE ORIGINAL

    
    ¿Por qué seria útil capturar sin mostrar el mensaje original?
    -------------------------------------------------------------

    Situación	                                Beneficio
    --------------------------------------------------------------------------
    Programas para usuarios finales	    No quieres mostrar mensajes técnicos 
                                        con traceback
    Aplicaciones con interfaz gráfica	Muestras un mensaje amigable: 
                                        'Hubo un problema'
    Juegos	                            Evitas que el jugador vea errores 
                                        internos
    Cuando ya sabes la causa	        No necesitas repetir información obvia

"""
try:
    a = 10 / 0

            # No capturamos el texto del error solo identificamos el tipo de 
            # error, anteriormente lo trabajabamos así 
            #       except ZeroDivisionError as e:  
            # donde "e" contenia el texto del error
except ZeroDivisionError:    
    print("Error!!! no se puede dividir entre cero")
