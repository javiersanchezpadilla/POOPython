""" LISTAS ENLAZADAS

    Es una colección lineal de elementos dedatos donde cada elemento de
    datos (nodo) apunta al siguiente,

    ELEMENTOS DE UNA LISTA
    -----------------------

        A --> B --> C --> D --> E       (A, B, C, D, E) Son Nodos
    Head                        Tail    --> Puntero o apuntador

    Head (Cabeza)   es el primer nodo en la lista ligada
    Tail (Cola)     es el último elemento de la lista ligada y no apunta
                    a ningún otro elemento.

    Existen dos tipos de listas enlazadas.
    --------------------------------------
    LISTA ENLAZADA SIMPLE.

        A --> B --> C --> D --> E --> F

    una lista enlazada simple donde cada nodo apunta al siguiente nodo con una 
    sola conexión, de una manera, sólo se puede ir de un nodo al siguiente, no 
    se puede volver al nodo anterior porque no hay conexiones ni punteros para 
    volver, sólo puedes ir del nodo 'A' al 'B', del 'B' al 'C', del 'C' al 'D'
    así así sucesivamente.  
    Y si quieres empezar a buscar de nuevo, tienes que volver a empezar por la 
    cabeza.
    La cabeza, el primer nodo de la lista, siempre será el punto de entrada a 
    la lista, algunas implementaciones también mantienen una referencia a la 
    cola de la lista.

    LISTA ENLAZADA DOBLE.

          -->   -->   -->   -->   -->  
        A     B     C     D     E    F
          <--   <--   <--   <--   <--  
    
    Y aquí podemos ver otra variación de la lista enlazada, que se llama lista 
    doblemente enlazada, es doble porque tiene dos referencias, esta referencia 
    permite que los nodos apuntan los unos a los otros para que puedas ir de 
    un nodo al siguiente y volver al anterior, como en una calle de doble 
    sentido.

    VENTAJAS DE LAS LISTAS ENLAZADAS.
    --------------------------------

    **) Los elementos (nodos) se pueden insertar fácilmente y eliminado 
        simplemente actualizando los punteros.
    **) Son dinámicos, por lo que su longitud puede aumentar o disminuir según 
        sea necesario.

    DESVENTAJAS DE LAS LISTAS ENLAZADAS.
    ------------------------------------

    Requieren más memoria que los arreglos, debido a que tienen que almacenar 
    referencias a otros nodos.

    INSERCIÓN DE NODOS.
    -------------------
    Existen tres formas de insertar un nodo.
    1)  Al inicio.
    2)  Enmedio de la lista
    3)  Al final de la lista

    Cuando se maneja el cocepto de inserciones se deben manejar los siguientes
    términos

    Head                                    Tail
        A --> B --> C --> D --> E --> F --> G

    Si queremos insertar el nodo 'Z' entre 'D' y 'E', se debe aplciar así

    Previous   Runner           'D' debe apuntar a 'Z' y 'Z' debe apuntar a 'E'
          D --> E               D --> Z --> E

"""                         
from E02_nodo import Nodo


class ListaEnlazada:

    def __init__(self):
        self.head = None

    def insertar_nodo(self, nuevo_valor):
        nuevo_nodo = Nodo(nuevo_valor)

        # INSERCIÓN DE LA CABEZA
        ''' Aquí se maneja cuando se define una nueva lista u cuando el valor
            del nuevo nodo es menor al valor del nodo HEAD, entonces debe
            cambiar el valor del nodo HEAD'''
        # Para el primer nodo insertado será la cabeza
        if self.head is None: 
            self.head = nuevo_nodo
        # si el valor es menor al nodo de la cabeza cambia la cabeza
        elif self.head.valor >= nuevo_valor:
            nuevo_nodo.siguiente = self.head
            self.head = nuevo_nodo
            
        else:
            ''' Insertar un nodo enmedio de la lista, se debe recorrer a la
                derecha cada par previous y runner hasta encontrar donde 
                será insertado'''
            previous = self.head            # primer nodo HEAD
            runner = self.head.siguiente    # siguiente nodo (dir de nodo 2)

            # mientras que no hemos llegado al final de la lista, por lo que 
            # el nodo runner, que es el nodo de la derecha no es None, y (and)
            # el nuevo valor que queremos es mayor que el valor del nodo 
            # actual, simplemente nos movemos a la derecha
            # aquí simplemente nos movemos en grupos de pares a la derecha
            # hasta encontrar la posición donde se debe insertar el nuevo nodo
            while (runner is not None) and (nuevo_valor > runner.valor):
                previous = runner
                runner = runner.siguiente

            nuevo_nodo.siguiente = runner   # nuevo nodo apunta al nodo runner
            previous.siguiente = nuevo_nodo # nodo previous apunta a nuevo nodo
