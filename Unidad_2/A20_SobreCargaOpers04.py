""" MÉTODOS ENRIQUECIDOS DE COMPARACIÓN.

    Comparar objetos basados en nuestro criterios, este tema tiene que ver con 
    la sobrecarga de los operadores dónde nosotros definimos el comportamiento 
    de los operadores ya sea para realizar las operaciones, las comparaciones, 
    las expresiones booleanas, etc.

    OPERADORES RELACIONALES.
    ------------------------
    __lt__  <	menor que
    __le__	<=	menor o igual que
    __qe__	==	Igual a
    __ne__	!=	Diferentes de
    __gt__	>	Mayor que
    __ge__	>= 	Mayor o igual que

    Cuando usamos un operador relacional, lo que sucede es que internamente se 
    están llamando a estos métodos que definen el comportamiento de la operación 
    de comparación.

    ¿CÓMO DETERMINAR SI UN CIRCULO ES MENOR QUE OTRO?

    Tenemos nuestro círculo, nuestro radio y el color del círculo, y queremos 
    determinar si un círculo es menor que otro.

    Creamos la clase para lo circulos y sobrecargamos los operadores de comparación.
"""
class Circulo:
    
    def __init__(self, radio, color):
        self.radio = radio
        self.color = color
    
    # Para las comparaciones <, >=. >, >= solo usamos el radio    
    def __lt__(self, other):
        return self.radio > other.radio
    
    def __le__(self, other):
        return self.radio <= other.radio and self.color == other.color
    
    def __gt__(self, other):
        return self.radio > other.radio
    
    def __ge__(self, other):
        return self.radio >= other.radio and self.color == other.color
    
    # para la condición de igualdad y diferencia tomaremos el radio y el color
    # ==   !=
    def __eq__(self, other):
        return (self.radio == other.radio and self.color == other.color)
    
    def __ne__(self, other):
        return (self.radio != other.radio or self.color != other.color)
    
    
# Creamosinstancias de circulo
circuloA = Circulo(5, "Azul")
circuloB = Circulo(5, "Verde")
circuloC = Circulo(7, "Rojo")
circuloD = Circulo(5, "Azul")

print(circuloA < circuloB)          # False
print(circuloA <= circuloD)         # True
print(circuloA <= circuloB)         # False mismo radio pero distinto color
print(circuloA != circuloC)         # True

