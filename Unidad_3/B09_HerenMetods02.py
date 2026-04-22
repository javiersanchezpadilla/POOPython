""" COMO LLAMAR MÉTODOS DE LA SUPERCLASE

    Poder llamar a un método de la superclase en la subclase es una de las 
    ventajas clave de la herencia en Python.

    Sintaxis:
    ---------
    Esta es la sintaxis general, donde ClassName es el nombre de la superclase

            ClassName.method_name(self, argumentos)

    Por ejemplo:

            Triangulo.encontrar_area(self)

    Sintaxis alternativa:
    ---------------------

    También puedes usar super() para referirte a la superclase.

            super().nombre_método(argumentos)

    Por ejemplo:

            super().encontrar_area()

    Aquí hay un ejemplo:
"""

class Triangulo:
 
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
	
    def encontrar_area(self):
        print((self.base * self.altura)/2)
 
 
class TrianguloDerecho(Triangulo):
	
    def muestra_area(self):
        print("=== Área del triangulo derecho ===")
 
        # Esta linea llama al método de la clase Triangulo.
        # super().encontrar_area()      # <-- Método alternativo
        Triangulo.encontrar_area(self)
 
		
right_triangle = TrianguloDerecho(5, 6)
right_triangle.muestra_area()

