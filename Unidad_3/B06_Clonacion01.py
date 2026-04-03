""" CLONACION

    Es el proceso de crear una copia exacta del objeto y esta copia es
    completamente independiente del objeto original.
    Es lo contrario a alising porque el nuevo objeto que creamos, el clon
    no está conectado con el objeto anterior. 

"""

a = [1, 2, 3, 4, 5, 6]
b = a[:]                # <---  Clonamos el objeto 'a'

print(id(a))            # Las direcciones son distintas, lo que nos dice
print(id(b))            # que son objetos distintos
