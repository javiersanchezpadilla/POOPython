""" LECTURA DE ARCHIVOS DE TEXTO

    Leer por caracteres
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"

archivo = open(ruta_archivo, 'r', encoding='utf8')

print(archivo.read(5))
print(archivo.read(3))
print(archivo.read(2))
print(archivo.read(15))

archivo.close()
