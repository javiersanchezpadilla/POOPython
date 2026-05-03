""" MANEJO DE EXCEPCIONES EN PYTHON (MANEJO DE ERRORES)

Tenemos varios niveles para el manejo de los errores. Un error o una excepción 
es cuando nuestro programa termina de forma abrupta, tenemos varios tipos de 
clases para el manejo de errores, (errores del tipo aritmético, del sistema 
operativo, de indentación, de sintaxis ) la clase exception es la clase padre 
que captura todos las excepciones y asu vez es hija de la clase BaseException.

                              BaseException
                                    ^
                                    |       (Clase padre que captura todas)
                                Exception   (las exepciones, es hija de) 
                                    ^       (BaseException)
                                    |
     +------------------+-------------+-----------------+--------------+
     ^                  ^             ^                 ^              ^
     |                  |             |                 |              |
AritmeticError      OSError      RunTimeError      LookupError     SintaxError
    ^                   ^                               ^              ^
    |                   |                               |              |
ZeroDivisionError       |                               |     IndentacionError
                        |                               |
               +-----------------+                +------------+
               ^                 ^                ^            ^
               |                 |                |            |
       FileNotFoundError   PermissionError    IndexError    KeyError


Ejemplo de una excepción. por ejemplo si queremos dividir un valor entre cero.

En código teclear lo siguiente y ejecutar
    10/0

Resultado
    Traceback (most recent call last):
    File "C:/CursosUniv/Python/Excepciones/Leccion01/Manejo_Excepciones.py", 
    line 1, in <module>
        10/0
    ZeroDivisionError: division by zero

Nos arroja la referencia de la clase ZeroDivisionError: y el error es division 
by zero
Esa es la subclase que procesa el error, pero podemos tratarla con cualquiera 
de sus clases padre

BaseException
      ^
      |
  Exception
      ^
      |
 AritmeticError
      ^
      |
ZeroDivisionError

Para poder atrapar el error, (lo que se conoce como try catch) es python se 
maneja como try except, con lo anterior vamos a capturar la excepción a través 
de una clase padre la 'clase Excepction'.
"""
resultado = None
a = 10
b = 0
try:
    resultado = a / b
    # Capturamos la excepcion (error) en una clase padre
    # podemos hacer pruebas ejecutando con las clase padre y el 
    # resultado será siempre el mismo

    # except BaseException as e:            
    # except ArithmeticError as e:

except Exception as e:
    print(f'Ocurrió un error {e}')

print(f'Resultado: {resultado}')
print('Continuamos...')

