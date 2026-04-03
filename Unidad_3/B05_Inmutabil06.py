""" ERROR COMÚN 

    tenga cuidado con los tipos de datos mutables como argumentos 
    predeterminados

    Consejo para los argumentos predeterminados:
    --------------------------------------------

    Evite el uso de tipos de datos mutables (como listas) como argumentos 
    predeterminados.

    ¿Por qué?
    Los argumentos predeterminados se inicializan cuando el intérprete de Python 
    interpreta inicialmente los métodos, por lo que solo hay una copia de cada 
    argumento predeterminado en la memoria.
    Los argumentos predeterminados no se crean cada vez que llama al método. En 
    cambio, se crean una vez cuando el programa comienza a ejecutarse.

    Listas como argumentos predeterminados
    --------------------------------------
    Si usamos una lista como argumento predeterminado, la referencia a la misma 
    lista se reutilizará para cada llamada al método.
    En el siguiente código, podemos ver cómo usamos una lista vacía como argumento 
    predeterminado para el parámetro de clientes en el método __init__().
    Es de esperar que esto funcione normalmente, creando una lista vacía (un 
    nuevo objeto) cada vez que crea una instancia.
    Pero esto no es lo que realmente sucede...
    Cuando comenzamos a agregar elementos a la lista, podemos ver que las dos 
    instancias se modificaron (consultar el ejemplo a continuación):

    Entre bastidores
    ----------------
    Lo que realmente sucede detrás de escena es que cuando se ejecuta esta 
    línea de código: 

            self.clientes.append(cliente)

    El nuevo cliente se agrega a la misma lista, no a una lista diferente para 
    cada instancia.
    Podemos comprobar que self.customers hace referencia a la misma lista con la 
    función id().

    Observe cómo los identificadores son exactamente iguales en los dos casos.
    SOLUCIÓN A ESTE PROBLEMA EN EL SIGUIENTE CÓDIGO B05_Inmutabil07.py
"""

class ListaDeEspera:
	
    # The default argument is an empty list.
    def __init__(self, clientes=[]):
        self.clientes = clientes
		
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

