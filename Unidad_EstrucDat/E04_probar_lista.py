""" PROGRAMA DE PRUEBAS

    En este ejercicio se hacen las pruebas de la clase E04_listas_enlazadas.py
"""

from E04_lista_enlazada import ListaEnlazada


mi_lista = ListaEnlazada()
print(mi_lista.head)

# Probamos la PARTE 1 del código (inserción de HEAD)
mi_lista.insertar_nodo(9)      # head 9
print(mi_lista.head)
print(mi_lista.head.valor)

mi_lista.insertar_nodo(3)      # head 3 --> 9 
print(mi_lista.head)
print(mi_lista.head.valor)

# Probamos la PARTE 2 del código (inserción enmedio o al final de la lista)
# Ahora probamos insertar un nodo enmedio
mi_lista.insertar_nodo(6)      # head 3 --> 6 --> 9 
print(mi_lista.head)
print('HEAD', mi_lista.head.valor)
print('midd', (mi_lista.head).siguiente.valor)
print('TAIL', ((mi_lista.head).siguiente).siguiente.valor)

print('\nMediante la notación de punto (para no usar tanto parentesis)')
print('HEAD', mi_lista.head.valor)
print('midd', mi_lista.head.siguiente.valor)
print('TAIL', mi_lista.head.siguiente.siguiente.valor)

# Ahora probamos insertar un nodo hasta el final de la lista
mi_lista.insertar_nodo(15)      # head 3 --> 6 --> 9 
print(mi_lista.head)
print('HEAD', mi_lista.head.valor)
print('midd', (mi_lista.head).siguiente.valor)
print('OLD TAIL', ((mi_lista.head).siguiente).siguiente.valor)
print('NEW TAIL', (((mi_lista.head).siguiente).siguiente).siguiente.valor)

print('\nMediante la notación de punto (para no usar tanto parentesis)')
print('HEAD', mi_lista.head.valor)
print('midd', mi_lista.head.siguiente.valor)
print('OLD TAIL', mi_lista.head.siguiente.siguiente.valor)
print('NEW TAIL', mi_lista.head.siguiente.siguiente.siguiente.valor)

# Probamos la PARTE 3 del código 
mi_lista.imprimir_elementos_lista()

# Probamos la PARTE 4.1 contar los nodos con ciclo para contar
print("El número de nodos en la lista son:", mi_lista.contar_nodos())
mi_lista.insertar_nodo(0) 
mi_lista.imprimir_elementos_lista()
print("El número de nodos en la lista son:", mi_lista.contar_nodos())

# PRobamos la PARTE 4.2 contar los nodos mediante la función recursiva
total_nodos = mi_lista.contar_nodos_recursiv()
print("El número de nodos en la lista son (recursiv):", total_nodos)
# mi_lista.insertar_nodo(0) 
# mi_lista.imprimir_elementos_lista()
# print("El número de nodos en la lista son:", mi_lista.contar_nodos())

# Probamos la PARTE 5 busqueda de un valor dentro de los nodos
print('Se encuentra el valor 6?', mi_lista.encontrar_valor_en_nodos(3))
print('Se encuentra el valor 6?', mi_lista.encontrar_valor_en_nodos(6))
print('Se encuentra el valor 6?', mi_lista.encontrar_valor_en_nodos(9))
print('Se encuentra el valor 6?', mi_lista.encontrar_valor_en_nodos(15))
print('Se encuentra el valor 6?', mi_lista.encontrar_valor_en_nodos(0))
print('Se encuentra el valor 6?', mi_lista.encontrar_valor_en_nodos(-9))

# PARTE 5 Borrado de valores dentro de la lista
#         borramos el primer elemento de la lista nodo HEAD
mi_lista.imprimir_elementos_lista()
print(mi_lista.borra_valor_en_nodos(0))
mi_lista.imprimir_elementos_lista()
print(mi_lista.borra_valor_en_nodos(100))
mi_lista.imprimir_elementos_lista()

# PARTE 5 Eliminamos un valor enmedio de la lista
mi_lista.imprimir_elementos_lista()
print(mi_lista.borra_valor_en_nodos(9))
mi_lista.imprimir_elementos_lista()

# PARTE 5 Eliminamos un valor al final de la lista
print(mi_lista.borra_valor_en_nodos(15))
mi_lista.imprimir_elementos_lista()

