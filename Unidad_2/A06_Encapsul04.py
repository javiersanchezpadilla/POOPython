"""Principio y justificación de la encapsulación

    Atributos publicos
"""

class Carro:

    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio 

mi_carro = Carro('Porsche', '911 carrera', 2020)
print(mi_carro.anio)

# El riesgo que podemos correr es que alguien cambie directamente 
# los valores, en este ejemplo el año se cambio a 5600, (un auto del futuro)
# en este momento no hay forma de validar si es correcto o no, y esto hace a
# nuestro código propenso a errores, ya que estos cambios inesperados
# pueden hacer que nuestro programa se interrumpa
mi_carro.anio = 5600
print(mi_carro.anio)

