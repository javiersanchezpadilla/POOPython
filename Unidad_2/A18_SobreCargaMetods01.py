"""" Python no tiene sobrecarga de métodos tradicional como la tienen lenguajes 
    como Java o C++.
    En otros lenguajes, puedes tener tres métodos con el mismo nombre pero con 
    diferentes "ingredientes" (parámetros). En Python, si escribes dos métodos 
    con el mismo nombre, el segundo borra al primero. """

class Calculadora:
    def __init__(self, nombre):
        self.nombre = nombre

    def suma(self, valor_a, valor_b):
        print(valor_a + valor_b)

    def suma(self, valor_a, valor_b, valor_c):
        print(valor_a + valor_b + valor_c)

    # En este caso vemos que el último método sobre escribe los anteriores
    def suma(self, valor_a, valor_b, valor_c, valor_d):
        print(valor_a + valor_b + valor_c + valor_d)


# --- Pruebas ---
calc = Calculadora("Mi Calculadora")

calc.suma(5, 5)             # Caso 1: dos argumento
calc.suma(10, 5, 5)         # Caso 2: tres argumentos
calc.suma(10, 5, 5, 10)     # Caso 3: cuatro argumentos
