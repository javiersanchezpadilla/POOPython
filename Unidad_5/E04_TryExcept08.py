""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    CAPTURAR EL ERROR ESPECIFICO SIN MOSTRAR EL MENSAJE ORIGINAL

    Ejemplo: Capturar valor inválido al convertir números
    En este ejemplo No le decimos al usuario 'IndexError: list index out of 
    range' (mensaje técnico propio de Python), solo le decimos 'índice fuera 
    de rango' (mensaje humano, personalizado y amigable).
    Se espera que el valor a convertir sea un por ejemplo una cadena de un
    valor numérico.

    Comparativa: Con mensaje original contra Sin mensaje original

        Versión	                    Código	              Lo que el usuario ve
    --------------------------------------------------------------------------
    Con mensaje original	except ZeroDivisionError as e:    division by zero
                                print(e)	

    Personalizado 	        except ZeroDivisionError:         Error
    (mi estilo)                 print("Error")	
   
    Personalizado avanzado	except ZeroDivisionError:         No se puede dividir 
                                print("No se puede dividir 	  entre cero
                                entre cero")


"""
def convertir_a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        print("No puedo convertir eso a número. Solo se permiten dígitos.")
        return 0

# Prueba
edad = convertir_a_entero("veinticinco")    # Muestra el mensaje personalizado
print(f"Edad usada: {edad}")                # Edad usada: 0
