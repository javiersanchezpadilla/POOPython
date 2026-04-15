""" HERENCIA  

    Herencia con constructor en la subclase
    En este ejemplo, la clase Perro hereda de la clase Animal y define su 
    propio constructor (__init__). 
    Al crear una instancia de Perro, se llama al constructor de Animal 
    utilizando super(), lo que permite inicializar el atributo nombre, y 
    luego se inicializa el atributo raza específico de Perro. 
    Esto demuestra cómo las subclases pueden extender la funcionalidad de la 
    clase padre al agregar su propia lógica de inicialización mientras aún 
    aprovechan el constructor del padre para

    El Sistema de Mascotas (Atributo Nuevo)
    ---------------------------------------
    En este caso, todos los animales tienen un nombre, pero solo los perros 
    tienen una raza. Usamos super() para que el padre guarde el nombre y el 
    hijo guarde la raza.
"""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Animal '{self.nombre}' registrado.")

class Perro(Animal):
    def __init__(self, nombre, raza):
        # 1. Le pedimos al padre que guarde el nombre
        super().__init__(nombre)
        # 2. Nosotros guardamos la raza (dato nuevo)
        self.raza = raza
        print(f"Es un perro de raza {self.raza}.")

# Creamos al perro pasando AMBOS datos
mi_mascota = Perro("Rex", "Pastor Alemán")
