""" ALIAS A LOS OBJETOS

    Las implicaciones o riesgos que podemos tener, es que si no sabemos
    de que fue creado este alias podemos hacer modificaciones sin 
    considerar que afectara al mismo objeto en memoria.
    Debemos ser precabidos de las consecuencias de crear varias referencias
    hacia el mismo objeto en memoria

"""

class Circulo:
    def __init__(self, radio):
        self.radio = radio

mi_circulo = Circulo(10)
tu_circulo = mi_circulo

# Podriamos pensar que es otro objeto pero no lo es
print(id(mi_circulo))
print(id(tu_circulo))
print(mi_circulo is tu_circulo)

# Aqui el riesgo si no sabemos que ambos son alias mi_circulo tu circulo
mi_circulo.radio = 100
print(tu_circulo.radio)
