""" GENERADORES (YIELD).

    OTRA FORMA DE CONSUMIR EL GENERADOR. Mediante un ciclo while.
    Tomamos todo el código creando una y otra vez el generador.
"""
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecución de la función')

# utilizamos el generador
generador = generador_numeros()
print(f'Objeto generador:{generador}')
print(type(generador))

for valor in generador:
    print(f'Numero producido: {valor}')

# consumir a demanda
# volvemos a cargar el generador para el consumo
generador = generador_numeros()
try:
    print(f'Cosumimos a demanda: {next(generador)}')
    print(f'Cosumimos a demanda: {next(generador)}')
    print(f'Cosumimos a demanda: {next(generador)}')
    print(f'Cosumimos a demanda: {next(generador)}')
    print(f'Cosumimos a demanda: {next(generador)}')
    # en este sexto valor se generara el error
    print(f'Cosumimos a demanda: {next(generador)}')
except StopIteration as e:
    print(f'Error al consumir generador {e}')

# Otra forma de consumir el generador.
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f'Impresion valor generado {valor}')
    except StopIteration as e:
        print('Se termino de iterar el generador')
        break

