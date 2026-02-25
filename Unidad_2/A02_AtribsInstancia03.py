""" Creación de atributos de instancia al vuelo

    Podemos crear atributos al vuelo sin pasar por __init__
"""

class Casa:

    def __init__(self, color):
        self.color = color


casa1 = Casa('Blanco')
casa2 = Casa('Cafe')

print(f'El color de la casa1 es {casa1.color}')
print(f'El color de la casa2 es {casa2.color}')

print('Imprimos el inventario de casa1')
print(casa1.__dict__)

print('Imprimos el inventario de casa2')
print(casa2.__dict__)

# Creamos un atributo para casa1, ahora el atributo 'precio' 
# es exclusico del objeto casa1
casa1.precio = 10000

print('Imprimos el inventario de casa1')
print(casa1.__dict__)

print('Imprimos el inventario de casa2')
print(casa2.__dict__)

