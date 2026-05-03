""" MANEJO EN ERRORES DE ELSE Y FINALLY.

    Podemos usar un bloque ELSE al final de todas las validaciones y solo se 
    ejecutará en caso de que no se haya encontrado ninguna condición de error, 
    si encuentra un error, será tratado por el bloque respectivo EXCEPT y ya 
    no se ejecutará el bloque ELSE, en otras palabras, en caso de que exista 
    un error y se llamara a uno de los bloques de control (except), ya no se 
    ejecutará el bloque ELSE.
"""
resultado = None

try:
    a = int(input('Primer valor: '))
    b = int(input('Segundo valor: '))
    resultado = a / b

except ZeroDivisionError as e:
    print(f'ERROR. Esta dividiendo entre cero')
    print(f'Error procesado por ZeroDivision en la clase {type(e)}')

except TypeError as e:
    print(f'ERROR. Operacion entre diferentes tipos de datos')
    print(f'Error procesado por TypeError en la clase {type(e)}')

except ValueError as e:
    print(f'ERROR. Valor no se puede convertir a entero')
    print(f'Error procesado por ValueError en la clase {type(e)}')

except Exception as e:
    print(f'ERROR. Generico')
    print(f'Error procesado por Exception en la clase {type(e)}')

else:
    print('NO SE ENCONTRO NINGUN TIPO DE ERROR!!!!')

print(f'Resultado: {resultado}')
print('Continuamos...')
