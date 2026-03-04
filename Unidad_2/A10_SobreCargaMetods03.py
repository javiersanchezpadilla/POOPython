""" Para la sobrecarga de Métodos, en Python usamos un truco más inteligente: 

    Un solo método que se adapta a lo que recibe.
    Ejemplo Práctico: El "Calculador de Área"
    Imagina que tienes una clase para calcular áreas. Quieres que el mismo 
    método calcular funcione si le das un solo dato (un Círculo) o si le das 
    dos datos (un Rectángulo).

    Así es como lo hacemos "al estilo Python":
    
    Resumen para los alumnos:
    A)  En Java/C++: Creas muchos métodos con el mismo nombre pero distintos 
        parámetros.
    B)  En Python: Creas un solo método muy flexible que usa if para decidir 
        qué hacer según lo que recibió.
"""

class Calculador:
    def __init__(self, nombre):
        self.nombre = nombre

    # Usamos valores por defecto (None) para simular la sobrecarga
    def calcular_area(self, medida1, medida2 = None):
        if medida2 is None:
            # Si solo recibimos un dato, asumimos que es un Círculo (Radio)
            area = 3.1416 * (medida1 ** 2)
            print(f"Área del Círculo: {area:.2f}")
        else:
            # Si recibimos dos datos, es un Rectángulo (Base y Altura)
            area = medida1 * medida2
            print(f"Área del Rectángulo: {area:.2f}")


calc = Calculador("Mi Calculadora")
calc.calcular_area(5)               # Caso 1: Un solo argumento
calc.calcular_area(10, 5)           # Caso 2: Dos argumentos