""" Ejemplo 02 

"""
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def find_diameter(self):
        return self.radius * 2


my_circle = Circle(10)
diameter = my_circle.find_diameter()
print(f'Diameter: {diameter}')
