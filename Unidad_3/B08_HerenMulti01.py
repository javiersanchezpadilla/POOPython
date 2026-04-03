""" HERENCIA MUTINIVEL EN PYTHON

    Herencia multinivel
    Con la sintaxis antes vista, podemos crear jerarquías más complejas con 
    múltiples niveles.
    Esto se llama herencia multinivel.

    Ejemplo de una jerarquía con tres niveles diferentes. Observe cómo pasamos 
    del concepto más general (Vehículo) a los conceptos más específicos (Coche y Camión).

                                             +----> Carro
                                            /
            Vehiculo ---> VehiculoTerrestre 
                                            \
                                             +----> Camión

    Representación de esta jerarquia en cóodigo
"""

class Vehiculo:
    pass
 
class VehiculoTerrestre(Vehiculo):
    pass
 
class Carro(VehiculoTerrestre):
    pass
 
class Camion(VehiculoTerrestre):
    pass
