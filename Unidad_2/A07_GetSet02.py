""" Los Getters y Setters permiten set y get values

    Trabajando con SETTERs

   los métodos que podemos llamar para asignar el valor a un atributi
   de instancia, esto lo haremos directamene a traves de un SETTER.
   La gran ventaja es que con los setters podemos validar el nuevo 
   valor antes de ser asignado al atributo de instancia.

    Sintaxis:
                set_ + <atributo>            <objeto>.set_<atributo>
    
    Ejemplos con atributos específicos:
    set_nombre      set_edad        set_direccion       set_id
    set_color       set_x           set_y               set_vida
    
"""
class Perro:

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
    

mi_perro = Perro('Solovino', 'Cafe')
print('Nombre de mi perro', mi_perro.get_nombre())
mi_perro.set_nombre('Max22')
print('Nombre de mi perro', mi_perro.get_nombre())
mi_perro.set_nombre('Max')
print('Nombre de mi perro', mi_perro.get_nombre())
