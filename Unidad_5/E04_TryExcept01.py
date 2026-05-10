""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    USO DE EXCEPT SIN ESPECIFICAR TIPO (CAPTURA CUALQUIER EXCEPCIÓN).

    Analogía para entender except: sin tipo
    ---------------------------------------
    Imagina que eres el guardia de seguridad de un edificio. Hay diferentes 
    tipos de emergencias:

    A)  Incendio (fuego)
    B)  Inundación (agua)
    C)  Terremoto (movimiento)

    Si usas un except ZeroDivisionError (tipo específico), es como tener un 
    extintor (solo apaga incendios). Si usas except: sin tipo, es como tener 
    un botón de pánico general que ante cualquier emergencia (fuego, agua, 
    temblor) simplemente dice: Algo anduvo mal, evacúen.

    En python cuando escribimos:

            try:
                # código peligroso
            except:
                # esto se ejecuta para CUALQUIER excepción

    Significa: Atrapa CUALQUIER ERROR que ocurra, sin importar su tipo.

    Reglas importantes a considerar
    ===============================

    Regla	                        Explicación
    --------------------------------------------------------------------------
    Es general	                Atrapa ZeroDivisionError, ValueError, 
                                IndexError, TypeError, ...(todos los erroeres)
    No sabes qué pasó	        No tienes acceso directo al mensaje de error.
    Puede esconder errores	    Si usas except: y no investigas, podrías 
                                ocultar fallos importantes.
    Bueno para limpieza	        Sirve cuando solo te importa que algo falló, 
                                no el tipo exacto.
    No es recomendado 	        Es mejor usar tipos específicos a menos que se 
    para todo                   tengas una buena razón.
"""

try:
    resultado = 10 / 0
except:
	print("Algo salió mal")
