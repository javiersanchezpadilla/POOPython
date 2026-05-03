""" MANEJO DE EXCEPCIONES, ÁMBITO Y ALCANCE DE LAS VARIABLES.

    Revisemos el siguiente programa. podemos ver que la variable resultado 
    esta declarada al inicio del programa (de los programas de pturba 
    anteriores), por lo que se una variable del tipo global.

        resultado = None        <-- Es del tipo global
        a = '10'
        b = 0
        try:
            resultado = a / b
        ...   ...   

    ¿Pero qué hubiera pasado si la variable resultado la hubiéramos declarado 
    dentro del bloque try?

    Resultado. como podemos apreciar se genera un nuevo tipo de error ya que 
    el ámbito de la variable es local dentro del bloque 'try', por lo que 
    debemos ser muy cuidadosos en este manejo, sin embargo si es posible 
    manejar las variables de los valores iniciales dentro del bloque. 
    (Solución en el siguiente ejempo)
"""
a = '10'
b = 0
try:
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
