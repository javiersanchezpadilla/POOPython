""" IMPORTAR MÓDULOS (Importar todo el contenido del módulo)

    Ahora, en el programa principal, escribimos la sentencia import, y el 
    nombre del módulo. Esto cargará el fichero como un objeto, pudiendo 
    acceder a través del punto a la variable, a la función y a la clase. 

"""

import B11_Imports01

print(B11_Imports01.variable)
B11_Imports01.mi_funcion()
B11_Imports01.MiClase()

print('A nivel ejecución yo programa B11_Imports02.py soy', __name__)
