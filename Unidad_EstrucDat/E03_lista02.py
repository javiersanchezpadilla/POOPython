""" PRÁCTICA

    Para practicar trabajando con nodos y sus atributos, crear las siguientes
    INSTANCIAS de nodos con los siguientes valores y apuntadores

    node_a: value = "a", next = node_b
    node_b: value = "b", next = node_c
    node_c: value = "c", next = node_d
    node_d: value = "d", next = None

    El resultado debe versa así:

    node_a -> node_b -> node_c -> node_d

"""
from E02_nodo import Nodo

node_d = Nodo('d')              # lo que estamos asignando a los nodos son
node_c = Nodo('c', node_d)      # instancias (no confundir, ya que los 
node_b = Nodo('b', node_c)      # ejemplos de listas enlazadas se realizarán
node_a = Nodo('a', node_b)      # sobre valores dentro de una misma INSTANCIA

print("Nodo 'a' valor = ", node_a.valor,"siguiente = ", node_a.siguiente )
print("Nodo 'b' valor = ", node_b.valor,"siguiente = ", node_b.siguiente )
print("Nodo 'c' valor = ", node_c.valor,"siguiente = ", node_c.siguiente )
print("Nodo 'd' valor = ", node_d.valor,"siguiente = ", node_d.siguiente )

print("\nComprobación de los enlaces de los nodos")
print("Nodo A con Nodo B", node_a.siguiente is node_b)
print("Nodo B con Nodo C", node_b.siguiente is node_c)
print("Nodo C con Nodo D", node_c.siguiente is node_d)
