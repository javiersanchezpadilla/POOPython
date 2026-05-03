""" MANEJO DE FINALLY

    Manejo de FINALLY, este bloque se ejecutará siempre al final de las 
    validaciones de excepciones sin importar si hay error o no se ejecuta, 
    se utiliza comúnmente para liberar recursos o informar al usuario del 
    resultado de las evaluaciones de las excepciones.
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

finally:
    print('SE CONCLUYÓ CON EL ANÁLISIS DEL MANEJO DE ERRORES O EXCEPCIONES')

print(f'Resultado: {resultado}')
print('Continuamos...')
