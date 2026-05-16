""" GENERADORES (YIELD).

    Consumiendo los valores del generador con un ciclo for
    ------------------------------------------------------
    Resultado. Podemos observar entonces que también utilizando un ciclo 'for' 
    sin ningún problema, podemos iterar cada uno de los valores, así que ya 
    sea que utilicemos la función de 'NEXT' para ir recuperando cada uno de 
    los valores o utilizando un ciclo 'FOR' para recuperar todos estos valores

    o de esta otra manera, asignamos la función a una variable, apuntamos la
    variable a la dirección de memoria de la función
"""
def generador():
    yield 1
    yield 2
    yield 3

gen = generador()       #asignamos una variable que apunta a la función

for valor in gen:
    print(f'Número generado: {valor}')

