""" GENERADORES (YIELD).

    Sin embargo si es posible volver a asignar este generador para utilizar de 
    nuevo sus valores.
"""
def generador():
    yield 1
    yield 2
    yield 3

print('Inicio del generador')
gen = generador()
print(next(gen))
print(next(gen))
print(next(gen))

print('Va de nuevo')
gen = generador()
print(next(gen))
print(next(gen))
print(next(gen))
