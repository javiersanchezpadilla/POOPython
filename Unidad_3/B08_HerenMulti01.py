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

    La Herencia Multinivel ocurre cuando una clase hereda de otra clase que, 
    a su vez, ya es una clase hija de otra. Es como un árbol genealógico: 
    
        Abuelo → Padre → Hijo.
"""

class Vehiculo:
    pass
 
class VehiculoTerrestre(Vehiculo):
    pass
 
class Carro(VehiculoTerrestre):
    pass
 
class Camion(VehiculoTerrestre):
    pass
