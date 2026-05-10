""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    CAPTURAR EL ERROR ESPECIFICO SIN MOSTRAR EL MENSAJE ORIGINAL

    Cuando existe mas deun error
    Cuando ocurre el primer error (división entre cero), el bloque try se 
    detiene inmediatamente y salta al except correspondiente. Los errores que 
    vienen después no se ejecutan.

    Tipos de captura
    ----------------
    Tipo de captura	        Código	                       Acceso 	Personaliz
                            al mensaje
    --------------------------------------------------------------------------
    Muy específica	        except ZeroDivisionError:	     No	          Sí
    Específica con mensaje	except ZeroDivisionError as e:	 Sí (usa e)	  Sí
    Genérica	            except:	                         No	          Sí
    Genérica con mensaje 	except Exception as e:	         Sí	          Sí

"""
try:
    a = 10 / 0          # ZeroDivisionError
    b = int("hola")     # ValueError (nunca llega aquí porque el primer error 
                        # detiene el try)

except ZeroDivisionError:
    print("Error de división")

except ValueError:
    print("Error de conversión")
