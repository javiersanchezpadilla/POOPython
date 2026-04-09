""" IMPORTAR MÓDULOS (Importar solo lo necesario)

    En vez de importar el módulo entero como un objeto, podemos importar 
    el contenido de este a través de la sentencia 'from'. Desde mi_modulo, 
    importamos la variable. Probamos a imprimir la variable y ejecutar la 
    función.

    En este ejemplo solo se importará la variable, por lo que no se tendrá
    acceso a nada mas, en caso de requerir mas elementos del módulo, por ejem.
    ademas de la varible la funcion, tenemos que incluirlo en la importacion

        from B11_Imports01 import variable, mi_funcion    
"""

from B11_Imports01 import variable

print(variable)
# mi_funcion()      # <-- ERROR no existe, solo se importo la variable
