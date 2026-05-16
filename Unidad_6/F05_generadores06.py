""" GENERADORES (YIELD).

    Veamos de nuevo desde otra perspectiva

"""
def generador():
    print('Se inicia le ejecución')
    yield 1
    print('Se reanuda la ejecución')
    yield 2
    print('Se reanuda finalmente la ejecución')
    yield 3

for valor in generador():
    print(f'Número generado: {valor}')

