""" METODOS QUE PROVOCAN MUTACIONES.

    Algo muy importante que debes saber es que algunos métodos integrados 
    en Python pueden mutar objetos.

            my_list = [6, 2, 7, 1]
            my_list.sort()
            print(my_list)              # [1, 2, 6, 7]

    Incluso si esto no era lo que pretendía hacer, el método .sort() mutó 
    la lista original en la memoria en lugar de devolver una nueva versión 
    ordenada de la lista.

    Para lograr esta misma funcionalidad sin mutar el objeto original, debes 
    usar la función sorted() en su lugar.

            my_list = [6, 2, 7, 1]
            print(sorted(my_list))      # [1, 2, 6, 7]
            print(my_list)              # [6, 2, 7, 1]

    Como puede ver, esta función devuelve una 'versión' ordenada de la lista 
    (una copia) sin modificar realmente la lista original, por lo que puede 
    continuar trabajando con ambas sin efectos secundarios involuntarios si 
    es necesario.

    Sugerencia
    ----------
    Recomiendo encarecidamente leer la documentación oficial antes de utilizar 
    un método integrado en su código para confirmar si causa alguna mutación.
    Si este fuera un proyecto real, tendrías un nuevo error hasta que te des 
    cuenta de que el método está causando esta mutación.

    Consejo: puedes comprobar si un método provoca una mutación en la 
    documentación oficial de Python.
"""

print('Uso del método .sort()')
my_list = [6, 2, 7, 1]
my_list.sort()
print(my_list)              # [1, 2, 6, 7]


print('\nUso de la funcion sorted()')
my_list = [6, 2, 7, 1]
print(sorted(my_list))      # [1, 2, 6, 7]
print(my_list)              # [6, 2, 7, 1]
