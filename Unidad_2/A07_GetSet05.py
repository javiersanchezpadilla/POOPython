""" Completamos el código del ejemplo de la calse Perro 
    aumentando los getters y setters para ambos atributos"""

class Perro:

    colores = ['Blanco', 'Negro', 'Cafe']

    def __init__(self, nombre, color):
        self._nombre = nombre       # Atributo no publico
        self.color = color          # Atributo publico

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nuevo_nombre):
        """ MEdiante el uso del Setter podemos hacer validaciones"""
        if isinstance(nuevo_nombre, str) and nuevo_nombre.isalpha():
            self._nombre = nuevo_nombre
        else:
            print('Por favor proporcine un nombre correcto')
    

    def get_color(self):
        # en el caso de los atributos públicos podemos acceder directamente
        # a ellos, pero si lo deseamos podemos crear getters para acceder
        # de forma indirecta
        return self.color
    
    def set_color(self, nuevo_color):
        # Nuevamente el atributo 'color' es público, y podemos accer
        # de forma directa para modificarlo, sin embargo es buena 
        # práctica hacerlo mediante setters
        if isinstance(nuevo_color, str) and nuevo_color in Perro.colores:
            self.color = nuevo_color
        else:
            print('Por favor proporcine un color correcto')


mi_perro = Perro('Solovino', 'Cafe')

print('Nombre de mi perro', mi_perro.get_nombre())
mi_perro.set_nombre('Max22')
print('Nombre de mi perro', mi_perro.get_nombre())
mi_perro.set_nombre('Max')
print('Nombre de mi perro', mi_perro.get_nombre())

print(mi_perro.color)
mi_perro.set_color('Violeta')

print(mi_perro.color)
mi_perro.set_color('Cafe')
print(mi_perro.color)

