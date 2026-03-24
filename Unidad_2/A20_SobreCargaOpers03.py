""" 

"""

class Estante:

    def __init__(self):  
        #  ubicacion donde esta localizado el libro
        self.contenido = [[],   # 1 es el Primer nivel
                          [],   # 2 es el Segundo nivel
                          []]   # 3 es el Tercer nivel
        
    def agregar_libro(self, libro, ubicacion):
        self.contenido[ubicacion].append(libro)

    def tomar_libro(self, libro, ubicacion):
        self.contenido[ubicacion].remove()

    def __getitem__(self, ubicacion):
        return self.contenido[ubicacion]
    

my_estante = Estante()

my_estante.agregar_libro('Los miserables', 0)
my_estante.agregar_libro('Orgullo y prejuicio', 0)
my_estante.agregar_libro('Frankestein', 0)

my_estante.agregar_libro('Dracula', 1)
my_estante.agregar_libro('Moby Dick', 1)
my_estante.agregar_libro('El libro vaquero',  1)

my_estante.agregar_libro('El principito', 2)
my_estante.agregar_libro('Huckleberry Finn', 2)
my_estante.agregar_libro('Kaliman', 2)

print(my_estante[0])
print(my_estante[1])
print(my_estante[2])
