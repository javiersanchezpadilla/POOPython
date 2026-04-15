""" ENLAZAR DOS VALORES DE FORMA MANUAL

    Mediante el uso de la clase Nodo, se enlazarán dos nodos de forma manual
    lo que estamos enlazando realmente son dos INSTANCIAS como si fueran
    una lista
"""

from E02_nodo import Nodo

nodo_2 = Nodo(2)

print(nodo_2.valor)
print(nodo_2.siguiente)

nodo_1 = Nodo(1, nodo_2)    # el nodo 1 apunta al nodo 2
print(nodo_1.valor)
print(nodo_1.siguiente)
print(nodo_1.siguiente is nodo_2)   # comprobamos que es la misma dir memoria

