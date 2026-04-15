""" OPERADOR ID CONTRA ==
"""

a = [1, 2, 3, 4, 5]     # Ambas listas tienen los mismos valores
b = [1, 2, 3, 4, 5]

print('¿Ambas listas tienen la misma direccioón de memoria?', a is b)
print('Direccion de la lista A', id(a))                     # False
print('Direccion de la lista B', id(b))                     # False

print('\n¿Ambas listas tienen los mismos valores?',a == b)  # True
