""" Elaboraremos el mismo ejemplo donde se explico el uso de self
    la diferencia es que ahora usaremos un atributo de clase"""

class Perro:

    numero_instancias = 0

    def __init__(self, nombre):
        self.nombre = nombre 
        Perro.numero_instancias += 1 
        self.numero = Perro.numero_instancias
        print(f'Dirección de memoria {Perro.numero_instancias}, de la instancia {self}')


perro1 = Perro('firulais')
perro2 = Perro('max')
perro3 = Perro('carnicero')
perro4 = Perro('canelo')

print('\n Imprimimos el numero de objeto con su dirección de memoria')
print('Perro1=', perro1.numero, '-', perro1.nombre, 'Memoria:', hex(id(perro1)))
print('Perro2=', perro2.numero, '-', perro2.nombre, 'Memoria:', hex(id(perro2)))
print('Perro3=', perro3.numero, '-', perro3.nombre, 'Memoria:', hex(id(perro3)))
print('Perro4=', perro4.numero, '-', perro4.nombre, 'Memoria:', hex(id(perro4)))
