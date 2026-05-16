""" LECTURA DE ARCHIVOS DE TEXTO

    Leer todas las líneas pero especificar qué línea queremos que se muestre.
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"

archivo = open(ruta_archivo, 'r', encoding='utf8')

print(archivo.readlines()[0])       # Leer el elemento cero de la lista

archivo.close()
