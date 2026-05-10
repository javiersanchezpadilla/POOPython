""" TRACEBACK

    El traceback es uno de los mensajes más importantes que verás como 
    programador Python, y saber leerlo es como aprender a leer un mapa del 
    tesoro que te dice exactamente dónde está el error.

    El traceback es el mensaje de error que Python muestra cuando un 
    programa falla, este mensaje contiene:

    1)  El tipo de error (ejemplo: ZeroDivisionError)
    2)  El mensaje descriptivo del error (ejemplo: division by zero)
    3)  La secuencia de llamadas que llevaron al error (la pista o rastro)

    Imagina que eres un detective en una escena del crimen. El traceback es 
    como el rastro de huellas que dejó el criminal: te dice por dónde pasó 
    (archivo, línea, función) y qué hizo finalmente (el error).

    EN LOS SIGUIENTES EJEMPLOS SE COMETERAN ERRORES PARA PODER EXPLICAR 
    EL CONCEPTO DE TRACEBACK

    Anatomía de un traceback (partes que lo componen)
    -------------------------------------------------
    Tomemos un error clásico de divisin entre cero 
    Vamos a desglosar pieza por pieza el error devuelto

    Parte del traceback	Significado	Ejemplo
    --------------------------------------------------------------------------
    Tipo de error	    Qué clase de error ocurrió	        ZeroDivisionError
    Mensaje de error	Descripción específica	            division by zero
    Archivo	            Dónde ocurrió	                    mi_programa.py
    Número de línea	    En qué línea exacta	                line 38
    Función/módulo	    Dentro de qué función	            en dividir
    Código ofensor	    La línea que causó el error	        return a / b
    Pila de llamadas	Secuencia de funciones que 	        Desde calcular() 
                        se llamaron                         hasta dividir()
    
    Para este ejemplo el traceback o ratreo es algo así:
    ----------------------------------------------------
    
    Traceback (most recent call last):
    File /home/javier/...../E05_traceback01.py, line 52, in <module> calcular()
    File /home/javier/...../E05_traceback01.py, line 49, in calcular
    resultado = dividir(10, 0)
                ^^^^^^^^^^^^^^
    File /home/javier/...../E05_traceback01.py, line 46, in dividir
    return a / b
           ~~^~~
    ZeroDivisionError: division by zero

    
    ¿Cómo leer el traceback paso a paso? (Método del detective)
    -----------------------------------------------------------
    Paso 1: Mira la última línea (el error real)
            ZeroDivisionError: division by zero
            Aquí sabes qué pasó y por qué.

    Paso 2: Sube una línea (dónde ocurrió exactamente)
            File "mi_programa.py", line 46, in dividir
                return a / b
            Aquí sabes el archivo, la línea y la función donde 
            ocurrió el error.

    Paso 3: Sigue subiendo (el camino que llevó al error)
            File "mi_programa.py", line 49, in calcular
                resultado = dividir(10, 0)
            Aquí ves qué función llamó a la que falló.

    Paso 4: Llega al inicio (la llamada original)
            File "mi_programa.py", line 52, in <module>
                calcular()
            Aquí ves desde dónde comenzó todo (el programa principal).

"""
def dividir(a, b):
    return a / b

def calcular():
    resultado = dividir(10, 0)
    print(resultado)

calcular()
