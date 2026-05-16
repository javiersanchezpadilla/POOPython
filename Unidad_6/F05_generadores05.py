""" GENERADORES (YIELD).

    Consumiendo los valores del generador con un ciclo for
    ------------------------------------------------------
    Resultado. Podemos observar entonces que también utilizando un ciclo 'for' 
    sin ningún problema, podemos iterar cada uno de los valores, así que ya 
    sea que utilicemos la función de 'NEXT' para ir recuperando cada uno de 
    los valores o utilizando un ciclo 'FOR' para recuperar todos estos valores

    El código puede quedar de está manera
"""
def generador():
    yield 1
    yield 2
    yield 3
                            # podemos directmante a la función generadora
for valor in generador():
    print(f'Número generado: {valor}')

