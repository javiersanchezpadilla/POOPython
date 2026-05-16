""" USO DE WITH, ARCHIVOS Y CONTEXT MANAGER EN PYTHON

    Hasta ahora para hacer uso de un archivo primero tenemos que abrirlo 
    (open) y al final debemos cerrarlo (close), cuando accedemos a un 
    archivo de la manera tradicional, es obligación cerrarlo, si hay un error 
    a mitad de camino, el archivo se queda abierto y secuestrado por la 
    memoria RAM.
    
    Sin embargo existe una manera simplificada y de forma automática va a 
    cerrar nuestro archivo, para manejar esto, a esto se le conoce como el 
    manejo de contexto WITH.
    La gran ventaja es que al usar el contexto WITH  de forma automática abre 
    el archivo y cierra el archivo, esto se conoce como CONTEXT MANAGER o 
    administrador de recursos.

        archivo = open("notas.txt", "w")
        archivo.write("Hola alumnos.")
                # Si aquí ocurre un error, la siguiente línea nunca se ejecuta
        archivo.close()

        
    El gestor de contexto with es una de las herramientas más elegantes de 
    Python. Su función principal es administrar recursos, un recurso (como un 
    archivo, una conexión a una base de datos o un puerto de red) se tiene 
    que solicitar al sistema operativo, usar y, lo más importante, devolver o 
    cerrar.
"""
archivo_ruta = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"

with open(archivo_ruta,'r', encoding='utf8') as archivo:
    print(archivo.read())

