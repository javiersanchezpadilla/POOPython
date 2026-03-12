""" El Concepto: ¿Por qué sobrecargar?

    Por defecto, Python no sabe cómo sumar dos objetos de una clase creada 
    por ti.
    Si tienes dos naves espaciales, ¿qué significa nave1 + nave2?
    ¿Sumar su tripulación?
    ¿Unir sus cargamentos?
    ¿Fusionar sus nombres?

    Tú, como programador, decides el significado de ese símbolo dentro de
    tu clase.

    Ejemplo Práctico: Clase Caja
    ----------------------------
    Imagina que tenemos cajas con un peso. Queremos que al usar el signo +, 
    obtengamos una nueva caja con la suma de los pesos.

    Operadores Comunes y sus Métodos Mágicos
    ----------------------------------------
    Tabla para identificar qué método deben usar según el símbolo:

    Operador    Método Mágico           Acción
    +           __add__(self, other)    Suma
    -           __sub__(self, other)    Resta
    *           __mul__(self, other)    Multiplicación
    ==          __eq__(self, other)     Igualdad (Comparación)
    <           __lt__(self, other)     Menor que
    >           __gt__(self, other)     Mayor que

"""
class Caja:
    def __init__(self, peso):
        self.peso = peso

    # SOBRECARGA DEL OPERADOR + (__add__)
    def __add__(self, otra_caja):
        nuevo_peso = self.peso + otra_caja.peso
                        # REgresa un nuevo objeto del tipo Caja
        return Caja(nuevo_peso)

    def __str__(self):
        return f"Caja de {self.peso}kg"

# --- Uso en el código ---
c1 = Caja(10)
c2 = Caja(20)

# Gracias a __add__, esto es posible:
c3 = c1 + c2 

print(c3)  # Resultado: Caja de 30kg
