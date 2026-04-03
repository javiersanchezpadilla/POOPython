""" SOLUCIÓN.

    Una solución a este problema es evitar el uso de una lista como argumento 
    predeterminado y usar esto en su lugar:

            class ListaDeEspera:
                                    
                def __init__(self, clientes=None):  <--- Clientes=None
                    if clientes is None:            <-- if clientes is None
                        self.clientes = []          <-- self.clientes = []
                    
                def agregar_cliente(self, cliente):
                    self.clientes.append(cliente)

    'None' se utiliza como argumento predeterminado, por lo que puede omitir 
    el argumento al crear la instancia.
    Si el valor de los clientes es Ninguno, el atributo se inicializa en una 
    lista vacía.
    De lo contrario, se asigna el valor pasado como argumento.
    Esto dará como resultado el comportamiento que esperaríamos:                    

    Ahora las instancias hacen referencia a dos listas separadas y modificar 
    una no modifica la otra.
"""

class ListaDeEspera:
	
    # The default argument is an empty list.
    def __init__(self, clientes=None):
        if clientes is None:
            self.clientes = []
		
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
 
# Creamos las instancias	
lista_de_espera1 = ListaDeEspera()
lista_de_espera2 = ListaDeEspera()
 
# Agregar un cliente a la primer lista de espera
lista_de_espera1.agregar_cliente("Javier")
 
# Ambos de ellos son modificados!
print(lista_de_espera1.clientes)        # Javier
print(lista_de_espera2.clientes)        # Javier

