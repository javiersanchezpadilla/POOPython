""" LISTAS ENLAZADAS.

    NODO.
    ======
    Un nodo puede almacenar dos elementos, un valor y una referencia a otro
    nodo (puntero).

    PUNTEROS.
    =========
    Los punteros son referencia a otro nodo en la estructura de datos.


    ¿QUÉ ES UNA LISTA ENLAZADA?
    ---------------------------
    Es una colección de elementos lineales dónde cada elemento (NODO) apunta 
    al siguiente elemento (NODO).

        A --> B --> C --> D --> E --> F

    Observemos que cada elemento está conectado con el siguiente elemento.
    Una estructura similar de uso común son los ARREGLOS en otros lenguajes de 
    programación, debido a que se ubican en la memoria de una forma continua y 
    ordenada, además se referencian a través de un índice, la gran ventaja que 
    ofrecen las listas con respeto a los arreglos es que no necesariamente es 
    requerido que los elementos están organizados en localidades de memoria 
    contiguas, los enlaces permiten acceder a los elementos de forma rápida.

    ELEMENTOS CLAVE PARA EL MANEJO DE LAS LISTAS ENLAZADAS.
    -------------------------------------------------------
    A)  HEAD (CABEZA) Es el primer nodo en una lista enlazada.
    B)  TAIL (Cola). El último nodo de una lista enlazada, este nodo ya no 
        apunta a ningún otro nodo.

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

"""



