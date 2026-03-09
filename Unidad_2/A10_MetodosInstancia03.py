""" Llamando a los metodos 

        < objeto > . <method > ( < argumentos > )

    Ejemplos:

    my_list = [4, 5, 6, 7, 8]
    print(my_list)              <-- [4, 5, 6, 7, 8]

    my_list.append(14)
    print(my_list)              <-- [4, 5, 6, 7, 8, 14]

    my_list.extend([1, 2, 3])
    print(my_list)              <-- [4, 5, 6, 7, 8, 14, 1, 2, 3]

    my_list.sort()
    print(my_list)              <-- [1, 2, 3, 4, 5, 6, 7, 8, 14]

    number = my_list.pop()
    print(number)               <-- 14
    print(my_list)              <-- [1, 2, 3, 4, 5, 6, 7, 8]

"""

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def find_diameter(self):
        print(f'Diameter: {self.radius * 2}')


my_circle = Circle(10)
my_circle.find_diameter()

