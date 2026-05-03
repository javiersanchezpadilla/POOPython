""" MANEJO DE EXCEPCIONES

    Sin embargo lo recomendable es hacer esta captura a un nivel más genérico, 

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
        
    ¿Qué pasa si el valor de la variable 'a' ya no es entero y se ahora es 
    cadena (a = '10') 
    Resultado. Como podemos ver ya cambió el tipo de error, ya no es división 
    entre cero, ahora es TypeError, el cual no corresponde a la clase 
    ZeroDivisionError, esto quiere decir que esta clase no puede procesar 
    errores del tipo 'type error', por esta razón es que manejamos una clase 
    padre genérica que abarque todos los errores.

    except Exception as e:
        
                                   +<-- AritmeticError <---- ZerodivisionError
                                   |
                                   |                    +<-- FileNotFoundError
                                   |                    |       
                                   +<-- OSError --------+
                                   |                    |
                                   |                    +<-- PermissionError
    BaseException <-- Exception <--+<-- RuntimeError
                                   |
                                   |                    +<-- IndexError
                                   |                    | 
                                   +<-- LoopUpError <---+
                                   |                    |
                                   |                    +<-- KeyError
                                   |
                                   +<-- SintaxError <------- IndentationError  

"""
resultado = None
a = '10'
b = 0
try:
    resultado = a / b
except Exception as e:
# except ZeroDivisionError as e:    # Así estaba originalmente
    print(f'Ocurrio un error {e}')

print(f'Resultado: {resultado}')
print('Continuamos...')

