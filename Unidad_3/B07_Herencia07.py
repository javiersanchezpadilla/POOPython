""" EJEMPLO DE HERENCIA

    Definiremos una clase empleado y una clase programador
"""


class Empleado:

    def __init__(self, nombre_completo, salario):
        self.nombre_completo = nombre_completo
        self.salario = salario


class Programador(Empleado):

    def __init__(self, nombre_completo, salario, lenguaje_de_programacion):
        Empleado.__init__(self, nombre_completo, salario)   # <-- podemos usar esto
        # super().__init__(nombre_completo, salario)        # <-- o esta sintaxis
        self.lenguaje_de_programacion = lenguaje_de_programacion


nora = Programador("Alberto Gutierrez", 30000, "Python")
print('Nombre completo', nora.nombre_completo)
print('Salario', nora.salario)
print('Lenguale', nora.lenguaje_de_programacion)
