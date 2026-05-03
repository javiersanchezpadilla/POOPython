""" MANEJO DE EXCEPCIONES

    Ahora bien ¿Por qué manejar una clase de mayor jerarquía en lugar de 
    manejar la clase hija que corresponde al tipo de error?
    vamos a suponer que uso directamente la clase que corresponde al al tipo 
    de error.

    BaseException           <-- Clase de mayor jerarquia
         ^
         |
      Exception             <-- Clase de mayor jerarquia
         ^
         |
    AritmeticError          <-- Clase de mayor jerarquia
         ^
         |
    ZeroDivisionError       <-- Esta es la clase especifica

    
        except BaseException as e:            
        except Exception as e:
        except ArithmeticError as e:

    Podemos capturar los errores a un nivel más específico, 
    
        except ZeroDivisionError as e:
            
    Revisar el siguiente código como continuación de la explicación
"""
resultado = None
a = 10
b = 0
try:
    resultado = a / b

    # Capturamos la excepcion (error) en una clase especifica correspondiente
except ZeroDivisionError as e:
    print(f'Ocurrio un error {e}')

print(f'Resultado: {resultado}')
print('Continuamos...')

