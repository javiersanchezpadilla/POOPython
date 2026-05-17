""" LECTURA DE ARCHIVOS DE TEXTO

    Abre el archivo datos.txt e imprime todo su contenido.

    La función open() y sus modos
    -----------------------------
    El primer argumento es la ruta; el segundo es el modo de apertura:

    1) 'r': Read (Lectura). Error si el archivo no existe.
    2) 'w': Write (Escritura). Crea el archivo o sobrescribe el contenido 
        actual.
    3) 'a': Append (Añadir). Escribe al final del archivo sin borrar lo 
        anterior.
    4) 'b': Binary (Binario). Para imágenes o ejecutables.

    NOTA: No olvidar abrir el archivo y cerrarlo despuúes de usarlo
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"

miVariable = open(ruta_archivo, 'r')    # <-- indicamos el modo lectura

contenido = miVariable.read()
print(contenido)
miVariable.close()
