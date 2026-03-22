""" Comparación de Objetos (__eq__ e __lt__)

    Imagina que estás evaluando estudiantes. No quieres comparar si son la 
    "misma persona" en memoria, sino si tienen el mismo promedio o quién 
    tiene mejor calificación.
"""
class Estudiante:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio

    # Sobrecarga de < (Menor que)
    def __lt__(self, otro):
        return self.promedio < otro.promedio

    # Sobrecarga de == (Igualdad)
    def __eq__(self, otro):
        return self.promedio == otro.promedio

# Uso
est1 = Estudiante("Antonio", 8.5)
est2 = Estudiante("Axel", 9.2)

print(est1 < est2)  # Resultado: True (8.5 es menor que 9.2)
print(est1 == est2) # Resultado: False
