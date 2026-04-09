from E04_lista_enlazada import ListaEnlazada


mi_lista_enlazada = ListaEnlazada()
print(mi_lista_enlazada.head)

mi_lista_enlazada.insertar_nodo(9)      # head 9
print(mi_lista_enlazada.head)
print(mi_lista_enlazada.head.valor)

mi_lista_enlazada.insertar_nodo(3)      # head 3 --> 9 
print(mi_lista_enlazada.head)
print(mi_lista_enlazada.head.valor)

# Ahora probamos insertar un nodo enmedio
mi_lista_enlazada.insertar_nodo(6)      # head 3 --> 6 --> 9 
print(mi_lista_enlazada.head)
print('HEAD', mi_lista_enlazada.head.valor)
print('midd', (mi_lista_enlazada.head).siguiente.valor)
print('TAIL', ((mi_lista_enlazada.head).siguiente).siguiente.valor)

print('\nMediante la notación de punto (para no usar tanto parentesis)')
print('HEAD', mi_lista_enlazada.head.valor)
print('midd', mi_lista_enlazada.head.siguiente.valor)
print('TAIL', mi_lista_enlazada.head.siguiente.siguiente.valor)


