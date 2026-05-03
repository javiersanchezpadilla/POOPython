""" LAS CLASES QUE CONTINUAN SON OPCIONEALES NO OBLIGATORIAS


MANEJO DE EXCEPCIONES

    Es un tema fundamental para pasar de escribir programas que 'corren' a 
    programas que son robustos y profesionales. En el mundo real, las cosas 
    fallan (el usuario escribe letras donde van números, se va el internet, un 
    archivo no existe), y las excepciones son la forma en que el software 
    maneja esos errores sin 'tronar'.


    1. ¿Qué es una Excepción?
    -------------------------
    Una excepción es un evento que ocurre durante la ejecución de un programa 
    y que interrumpe el flujo normal de las instrucciones. No es 
    necesariamente un error de dedo del programador, sino una situación 
    excepcional que el sistema debe saber gestionar.

    Analogía: Imagina que vas conduciendo hacia el tecnológicola. Si se poncha 
    una llanta (Excepción), no abandonas el auto; sacas la refacción, la 
    cambias (Manejo de la excepción) y sigues tu camino.

    2. Estructura: El Bloque try - except
    -------------------------------------
    En Python, el manejo de excepciones se basa en cuatro palabras clave:
    1)  try: Aquí pones el código que puede fallar.
    2)  except: Aquí pones el código que se ejecutará solo si ocurre un error.
    3)  else (opcional): Se ejecuta solo si no hubo errores en el try.
    4)  finally (opcional): Se ejecuta siempre, haya habido error o no (ideal 
        para cerrar archivos o bases de datos).

    Ejemplo Práctico y clásico: División Segura
    --------------------------------------------
    Este es el ejemplo clásico para el pizarrón. Muestra cómo evitar que el 
    programa se detenga si el usuario ingresa un cero o una letra.
"""
def dividir():
    try:
        n1 = float(input("Ingresa el dividendo: "))
        n2 = float(input("Ingresa el divisor: "))
        resultado = n1 / n2
    except ZeroDivisionError:
        print("Error: No puedes dividir entre cero.")
    except ValueError:
        print("Error: Debes ingresar números, no letras.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    else:
        print(f"El resultado es: {resultado}")
    finally:
        print("Operación finalizada.")

dividir()
