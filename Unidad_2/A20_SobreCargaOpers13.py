""" Un ejemplo de Comparación (Nivel Intermedio)

    No solo podemos sumar; también podemos enseñar a los objetos a 
    compararse entre sí. Por ejemplo, saber qué Automovil es más potente:

    "Sobrecargar operadores es como darle un diccionario nuevo a Python. 
    Antes, Python solo sabía sumar números. Ahora, gracias a los métodos 
    mágicos, le enseñaste que 'sumar' también puede significar 'acoplar 
    dos vagones de tren' o 'mezclar dos colores'."
    
"""

class Automovil:
    def __init__(self, modelo, hp):
        self.modelo = modelo
        self.hp = hp

    # SOBRECARGA DEL OPERADOR > (__gt__ de Greater Than)
    def __gt__(self, otro):
        return self.hp > otro.hp    # retorna True o False

# --- Pruebas ---
auto1 = Automovil("Sedán", 150)
auto2 = Automovil("Deportivo", 450)

if auto2 > auto1: # Python usa __gt__ internamente aquí
    print(f"El {auto2.modelo} es más potente que el {auto1.modelo}")
