""" CREACIÓN DE CLASE DE EXCEPCIÓN PERSONALIZADA (Continuación).

    Ahora regresamos a nuestro programa principal y para poder utilizarla 
    tenemos que importarla, así como validamos el error, para lanzar la 
    excepcion tenemos que usar la palabra reservada raise con la clase creada 
    y el mensaje, recordemos que nuestra clase creada pertenece a la clase 
    padre Exception por lo que a partir de este momento se procesa el bloque 
    (except Exception as e:).

"""
from E01_Excepciones10 import NumerosIdenticosException

resultado = None
try:
    a = int(input('Primer valor: '))
    b = int(input('Segundo valor: '))
    if a == b:
        raise NumerosIdenticosException('Numeros Identicos')
        # Tambien podemos personalizar el error 
        # raise ValueError('Los valores son iguales')
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
    print('SE CONCLUYO CON EL ANALISIS DEL MANEJO DE ERRORES O EXCEPCIONES')


print(f'Resultado: {resultado}')
print('Continuamos...')
