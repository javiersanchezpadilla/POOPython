""" MANEJO DE EXCEPCIONES (CLASES DE EXCEPCION MAS ESPECIFICAS)

   Procesar Clases de excepción más específicas. Si queremos procesar de 
   forma específica el tipo de error, conociendo las posibilidades que 
   pudieran presentarse de acuerdo al tipo de error podemos hacer lo siguiente


                                   +<-- AritmeticError <---- ZerodivisionError
                                   |
                                   |                    |<-- FileNotFoundError
                                   +<-- OSError --------+
                                   |                    |<-- PermissionError
                                   |
    BaseException <-- Exception <--+<-- RuntimeError
                                   |                    |<-- IndexError
                                   +<-- LoopUpError <---+
                                   |                    |<-- KeyError
                                   |
                                   +<-- SintaxError <------- IndentationError  

"""
resultado = None
a = '10'
b = 0
try:
    resultado = a / b

except ZeroDivisionError as e:
    print(f'Ocurrio un error {e}')
except TypeError as e:
    print(f'Ocurrio un error {e}')

print(f'Resultado: {resultado}')
print('Continuamos...')
