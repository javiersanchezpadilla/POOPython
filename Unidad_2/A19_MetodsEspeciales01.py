""" METODOS ESPECIALES.

    Los métodos especiales se llaman especiales porque tienen como una sintaxis
    especial que puedes usar en Python, puedes llamarlos indirectamente sin 
    usar sus nombres explícitamente, sólo usando los operadores normales de Python.
    Son muy interesantes, aprenderemos sobre los métodos especiales en Python,
    sus casos de uso, y cómo definirlos para personalizar lo que hacen para tus
    clases personalizadas.
    También se aprenderá por qué se llaman métodos dunder, que es bastante curioso, 
    y los más importantes, como los que normalmente te gustaría personalizar para 
    tus clases.

    Los métodos especiales tienen guiones bajos dobles al principio y al final de 
    u nombres. Por ejemplo: __str__.

    Python los llama automáticamente cuando se realizan ciertas operaciones o cuando 
    se utiliza una sintaxis específica.
    Le permiten personalizar el comportamiento de sus objetos para operaciones 
    integradas. Por ejemplo, obtener la longitud de un objeto y agregar objetos 
    de un tipo específico.

    __init__( )     también es un método especial. Se llama automáticamente 
                    cuando una instancia de una clase es creada.

    Algunos ejemplos de métodos especiales son:
    -------------------------------------------
    __str__() 	    para obtener una representación del objeto fácil de usar.
    __repr__() 	    para obtener una representación del objeto fácil de usar para
                    el desarrollador.
    __len__() 	    para obtener la longitud de un objeto.
    __add__() 	    para agregar dos objetos.
    __getitem__()   para obtener un elemento de un objeto, como si fuera una
                    secuencia.
    __bool__() 	    para hacer que el objeto se evalúe como Verdadero o Falso,
                    basado en una condición específica.
    __iter__() 	    para convertir un objeto en iterable.
    __next__() 	    para recuperar el siguiente elemento de un iterador.

    Por ejemplo, en Python, para sumar dos números, como por ejemplo, cinco y 
    seis utilizando el operador más (+), pero en realidad detrás de las escenas 
    estamos llamando al método __add__( ) de la clase integer para realizar esta 
    operación, en realidad no estamos llamando a este método, no escribimos 
    __add__(5,6), sólo estamos escribiendo esta operación utilizando el operador 
    más (+) y detrás de las escenas, este método está siendo llamado.
"""

#  estamos llamando al método __add__( ) de la clase integer para realizar esta 
#  operación
print(5 + 6)

print((5).__add__(6))

