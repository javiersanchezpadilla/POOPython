""" MANEJO DE EXCEPCIONES, ÁMBITO Y ALCANCE DE LAS VARIABLES.

    Manejando las variables con los valores dentro del bloque

    Provocaremos los siguientes errores:
    ------------------------------------
    1)  ERROR 1 Vamos a solicitar los valores por teclado, pero recordemos
        que las capturas desd teclado deben convertirse a valores enteros, 
        entonces para provocar un error no lo vamos a hacer en la segunda 
        variable 
    2)  ERROR 2 Una vez corregido el error, vamos a capturar valores que no
        sean numéricos capturaremos una letra “a” en uno de los dos valores 
        solicitados, lo que observaremos es que ahora el error será procesado
        Por la clase Genérica de mayor jerarquía 'Exception', pero el error 
        corresponde a la clase 'ValueError', la cual si queremos podríamos 
        incluir como parte del manejo de error específico, si queremos ser mas
        específicos tenemos que agregar a nuestro programa la sig. excepción
                   vvvvvvvvvv
            except ValueError as e:
                print(f'ERROR. Valor no se puede convertir a entero')
                print(f'Error procesado por ValueError en la clase {type(e)}')

    Con todo lo anterior ya sabemos del manejo específico de las excepciones, 
    por lo que podemos manejar a detalle las excepciones sin olvidar que 
    primero se consideran las clases de menor jerarquía y al final la clase de 
    mayor jerarquía para el manejo de los errores. 
    
    VERSION GENERAL PARA RESOLVER ESTE CÓDIGO:
    ------------------------------------------

            resultado = None
            try:
                a = int(input('Primer valor: '))
                b = int(input('Segundo valor: '))
                resultado = a / b
            except Exception as e:          <-- Está clase (excepcion) abarca
                print(f'ERROR. {e}')            a todas las específicas
"""
resultado = None

try:
    a = int(input('Primer valor: '))
    b = input('Segundo valor: ')	    # <--- ERROR 1 provocaremos un error
    # b = int(input('Segundo valor: '))   # corrección del error
    resultado = a / b

except ZeroDivisionError as e:
    print(f'ERROR. Esta dividiendo entre cero')
    print(f'Error procesado por ZeroDivision en la clase {type(e)}')

except TypeError as e:
    print(f'ERROR. Operacion entre diferentes tipos de datos')
    print(f'Error procesado por TypeError en la clase {type(e)}')

except Exception as e:
    print(f'ERROR. Generico')
    print(f'Error procesado por Exception en la clase {type(e)}')

print(f'Resultado: {resultado}')
print('Continuamos...')
