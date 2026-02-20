""" Aqui se entinde aún mejor el uso de self

    Cada objeto tiene una dirección en memoria y 'self' dependiendo de la
    instancia apuntara a ella
"""


class Perro:

    def __init__(self, nombre):
        print(self)                 # aqui vemos que 'self' apunta a la DIR
        self.nombre = nombre
        

perro01 = Perro('firulauis')        
perro02 = Perro('Negro')
perro03 = Perro('Carnicero')

print('Imprimimos las direcciones de memoria de cada objeto')
print('La direccion de perro01 es', hex(id(perro01)))
print('La direccion de perro02 es', hex(id(perro02)))
print('La direccion de perro03 es', hex(id(perro03)))

