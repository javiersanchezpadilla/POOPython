""" GENERADORES (YIELD).

    Podemos consumir los datos a demanda de acuerdo a como los necesitemos.
"""
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecución de la función')

generador = generador_numeros()
print(f'Cosnumimos a demanda: {next(generador)}')
print(f'Cosnumimos a demanda: {next(generador)}')
print(f'Cosnumimos a demanda: {next(generador)}')

