""" MANEJO DE EXCEPCIONES (CLASES DE EXCEPCION MAS ESPECIFICAS)

   Manejo de excepciones específicas y excepciones genéricas, podemos atrapar 
   excepciones específicas para su tratamiento, sin embargo podemos incluir un 
   manejo general para atrapar aquellos errores que no estaban considerados en 
   el manejo específico de los errores, lo único que hay que respetar es que la 
   excepción general que corresponde a una clase de mayor jerarquía debe 
   indicarse al final de las excepciones o de lo contrario atrapará primero el 
   error sin tomar en cuenta a las excepciones específicas. Entonces aplicando 
   que las clases más genericas deben de ir al final y al inicio las clases 
   más espeficas.
"""
resultado = None
a = 10
b = 0
try:
    resultado = a / b
except ZeroDivisionError as e:
    print(f'ERROR. Está dividiendo entre cero ->{e}')
    print(f'Error procesado por ZeroDivision en la clase {type(e)}')

except TypeError as e:
    print(f'ERROR. Operación entre diferentes tipos de datos -> {e}')
    print(f'Error procesado por TypeError en la clase {type(e)}')

except Exception as e:          # la clase exception se colocal al fina para
                                # no atrape el error antes que los especificos
                                # podemos probar colocandola al inicio, lo que
                                # ocasionará que jamas se puedan ver los otros
                                # tipos de validación de errores
    print(f'ERROR. -> {e}')
    print(f'Error procesado por Exception en la clase {type(e)}')

print(f'Resultado: {resultado}')
print('Continuamos...')
