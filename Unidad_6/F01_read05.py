""" LECTURA DE ARCHIVOS DE TEXTO

    Lectura de Datos
    ----------------
    Hay tres formas principales de leer, dependiendo de la memoria disponible:

    1)  read(): Lee todo el archivo en un solo string (Cuidado con archivos 
        Gigantes).
    2)) readline(): lee por linea el archivo (una a una por demanda)
    3)  readlines(): Devuelve una lista donde cada elemento es una línea.
    4)  Iteración directa (Recomendado): Muy eficiente en memoria.

    READLINE()
    ----------
    Leer línea por línea, al final de la línea inserta una línea en blanco 

    Abre el archivo datos.txt e IMPRIME SOLO LA PRIMER LINEA
    NOTA: No olvidar abrir el archivo y cerrarlo despuúes de usarlo
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"
miVariable = open(ruta_archivo)

contenido = miVariable.readline()
print(contenido)
miVariable.close()
