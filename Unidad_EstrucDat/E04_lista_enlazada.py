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

        ''' PARTE 1. INSERCIÓN DEL NODO HEAD (INICIAL)
                     Aquí se maneja cuando se define una nueva lista u cuando 
                     el valor del nuevo nodo es menor al valor del nodo HEAD, 
                     entonces debe cambiar el valor del nodo HEAD'''
        # Para el primer nodo insertado será la cabeza
        if self.head is None: 
            self.head = nuevo_nodo
        # si el valor es menor al nodo de la cabeza cambia la cabeza
        elif self.head.valor >= nuevo_valor:
            nuevo_nodo.siguiente = self.head
            self.head = nuevo_nodo
            
        else:
            ''' PARTE 2 INSERCIÓN DE UN NODO INTERMEDIO O AL FINAL DE LA LISTA
                        Insertar un nodo enmedio de la lista, se debe recorrer 
                        a la derecha cada par previous y runner hasta encontrar
                        donde será insertado.
                        Está lógica también incluye la inserción de un nodo al 
                        final de la lista'''
            previous = self.head            # primer nodo HEAD
            runner = self.head.siguiente    # siguiente nodo (dir de nodo 2)

            # interpretación del ciclo While:
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

    def imprimir_elementos_lista(self):
        """ PARTE 3 Imprimira todos los elementos o los valores de los nodos 
                    de la lista enlazada en la misma linea en una secuencia 
        """
        # Verificamos que la lista no este vacia
        if self.head is None:
            print("Lista vacia")
        # Si no esta vacia entonces recorremos elemento por elemento de la lista
        else:
                                                # Asignamos HEAD a runner
            runner = self.head                  # runner ahora es eñ nodo actual
            while runner is not None:
                print(runner.valor, end=" --> ")
                runner = runner.siguiente

            print()

    def contar_nodos(self):
        """ PARTE 4.1 permite contar el número de nodos dentro de la lista
                      Solución mediante un ciclo que permitirá recorrer los 
                      elmentos de la lista uno a uno"""
        contador = 0
        runner = self.head

        while runner is not None:
            contador += 1
            runner = runner.siguiente
        
        return contador
    
    def contar_nodos_recursiv(self):
        """ PARTE 4.2.1 Esta función se crea para llamar a la verdadera 
                        función que resuelve que es 
                        contar_recursivamente(self), así el usuario no tiene
                        que indicar ningún argumento de llamada"""
        return self.contar_recursivamente(self.head)


    def contar_recursivamente(self, nodo):
        """ PARTE 4.2 Implementación del conteo de nodos pero con una función 
                      recursiva (es mas eficiente), el problema es que para 
                      poder ejecutar esta llamada el ususario tendria que 
                      escribir para indicar el nodo HEAD (refencia del primer
                      nodo):

                      mi_lista.contar_nodos_recursiv(mi_lista.head)

                      Lo cual se vuelve impractico, para evitar al usuario que
                      tenga que escribir (mi_lista.head) hacemos la llamada
                      de forma indirecta, por lo que se va a crear la función
                      contar_noodos_recursivamente(), la cual será la que el 
                      usuario llamara sin argumentos, y esta a su vez llamará
                      a la verdadera función recursiva
        """
        if nodo is None:
            return 0
        else:
            return 1 + self.contar_recursivamente(nodo.siguiente)
    

    def encontrar_valor_en_nodos(self, valor_a_buscar):
        """ PARTE 5. Busqueda de un valor en uno de los nodos"""
        runner = self.head

        while runner is not None:
            if runner.valor == valor_a_buscar:
                return True
            runner = runner.siguiente

        return False
    
    def borra_valor_en_nodos(self, valor_a_borrar):
        """ PARTE 5. Borrado de un valor encontrado en uno de los nodos
                     retorno:
                     True Si eliminó un nodo con ese valor
                     False Si no encontro el valor dentro de la lista"""
        # En caso de la lista este vacia, no hay nada que borrar
        if self.head is None:
            return False
        # En caso de que el valor a borrar sea el primer nodo (HEAD)
        elif self.head.valor == valor_a_borrar:
            self.head = self.head.siguiente
            return True
        # Cuando el valor se encuentra enmedio de la lista, se requiere 
        # enlazar el nodo previo con el nodo adelante del valor encontrado
        # para que se desvincule dentro de la lista y de esta manera ya no
        # tendrá acceso a ese valor.
        # Está implementación tambien funciona cuando el valor se encuentra
        # al final de la lista
        else:
            previous = self.head
            runner = self.head.siguiente

            while (runner is not None) and (valor_a_borrar > runner.valor):
                previous = runner
                runner = runner.siguiente

            if (runner is not None) and(runner.valor == valor_a_borrar):
                # previous ahora apuntará al nodo que se encuentra
                # después del nodo runner.
                # Cuando el valor a borrar es el último valor el valor que
                # toma previous.siguiente = runner.siguiente será None
                previous.siguiente = runner.siguiente  # Creamos el puennte
                return True
            else:
                return False
            
    def imprime_reversa(self):
        """ to implement them, a nice challenge would be to implement the 
            method print_reversed() to print the linked list in reverse order.
            For example, if the current state of the linked list is:
            3 -> 5 -> 8 -> 15 -> 26 -> 35  Salida   35 26 15 8 5 3
            With the values separated by a space.

            Recomendación:
            Recursion can be very helpful to implement this method.
            You could print the values on the same line by passing end=" " as 
            the second argument of the call to print().
        """
        pass


