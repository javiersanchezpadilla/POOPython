""" RAISE

    ¿Qué es raise? 
    ---------------
    raise es la palabra clave en Python para generar una excepción manualmente
    Es como si dijeras: Aquí, en este punto del código, decido que algo va mal 
    aunque Python no lo vea como error automático.

    Cuatro formas de usar raise
    ---------------------------

    Forma	                        Código	                        ¿Qué hace?
    --------------------------------------------------------------------------
    Con mensaje 	    raise ValueError("Mensaje       Crea una nueva excepción 
    personalizado       personalizado")                 con tu mensaje

    Relanzar la 	    raise (solo, sin nada más)	    Vuelve a lanzar la excepción 
    última excepción                                    que acaba de ocurrir
    Sin mensaje 	    raise TypeError	                Lanza la excepción con 
    (solo el tipo)                                      su mensaje por defecto

    Con mensaje 	    raise ZeroDivisionError	        Igual que la 1, pero con 
    específico          ("No se puede dividir")         otro tipo de error


    raise TipoError("Mensaje personalizado")

    Sintaxis: 
            raise NombreDeLaExcepcion("texto personalizado")

    ¿Cuándo usarlo?
    ---------------
    **) Cuando validas datos de entrada
    **) Cuando una condición específica no se cumple
    **) Cuando quieres dar un mensaje claro al usuario o programador
"""
def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 120:
        raise ValueError("La edad no puede ser mayor a 120 años")
    return f"Edad válida: {edad}"

# Probamos
try:
    validar_edad(-5)
except ValueError as e:
    print(f"Error capturado: {e}")
