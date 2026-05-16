""" GENERADORES (YIELD).

    Si queremos proteger la posibilidad de error usamos un bloque try catch, 
    por ejemplo en el programa anterior permite extraer del generador un 
    máximo de cinco valores del 1 al 5, pero qué sucede si intentamos extraer 
    un sexto valor?
"""
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecución de la función')

# utilizamos el generador
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

