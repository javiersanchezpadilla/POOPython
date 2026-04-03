""" INMUTABLE NO SIGNIFICA QUE SUS ELEMENTOS SEAN INMUTABLES.

    Los objetos inmutables pueden contener objetos mutables.
    Por ejemplo, podríamos tener una lista dentro de una tupla.
    Estos objetos mutables se pueden modificar incluso si sus contenedores 
    no se pueden modificar.

    He aquí un ejemplo que ilustra esto. Tenemos esta lista inicial:

    mi_lista = ([1, 2, 3], "abc", 56)

    Si intentamos cambiar un elemento de la tupla, obtenemos un error porque 
    las tuplas son objetos inmutables:

            TypeError: el objeto 'tupla' no admite la asignación de elementos

    Pero si profundizamos aún más e intentamos modificar los elementos de un 
    elemento de la tupla que sea mutable, no obtendremos ningún error.
    Aquí estamos cambiando el segundo elemento, el primer elemento de la tupla 
    (la lista). Estamos reemplazando el número 2 de la lista [1, 2, 3] por el 
    número 4 ([1, 4, 3]).
    Esta sera la salida:

            ([1, 4, 3], 'abc', 56)

    Va a cambiser sin errores.
    La conclusión clave es que elegir un objeto 'contenedor' inmutable (por 
    ejemplo, una tupla) realmente no 'protege' los elementos en sí del cambio 
    si son mutables (por ejemplo, listas).
"""

mi_lista = ([1, 2, 3], "abc", 56)

mi_lista[0][1] = 4      # Cambiamos el 2 por el 4 dentro de la lista
print(mi_lista)         # Salida ([1, 4, 3], 'abc', 56)

