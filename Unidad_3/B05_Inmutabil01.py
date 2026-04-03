""" MUTABILIDAD INMUTABILIDAD.

    Mutación. es una alteracion básica o significativa de algo

             +--- Mutable (PUEDE ser modificado)
             |
    OBJETOS -+
             |
             +--- Inmutable (NO PUEDE ser modificado)

             
    TIPOS DE OBJETOS:         
    MUTABLES    --> Listas      Conjuntos   Diccionarios

    INMUTABLES  --> Booleanos   Enteros     Flotantes   
                    Cadenas     Tuplas

    Ventajas y desventajas del uso de objetos mutables e inmutables:
    ----------------------------------------------------------------

    OBJETOS MUTABLES:

    1) VENTAJAS:    Poder reusar objetos existentes en lugar de tener que 
                    realizar nuevas copias para cada cambio.
    2) DESVENTAJAS: El uso de objetos mutables en un programa puede 
                    introducir errores (bugs), porque podrias de forma
                    involuntaria mutar un objeto en el programa.

    Por ejemplo suponer que queremos mantener una lista intacta, pero 
    requerimos la suma absoluta de los valores de la lista, el error en
    este programa es que al final estamos mutando la lista que pasamos 
    como argumento
"""

def suma_valores_absolutos(secuencia):
    for i in range(len(secuencia)):
        secuencia[i] = abs(secuencia[i])
    return sum(secuencia)


valores = [-5, -6, -7, -8]
print(valores)
print(suma_valores_absolutos(valores))
print(valores)


