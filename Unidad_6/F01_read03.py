""" LECTURA DE ARCHIVOS DE TEXTO

    Agregar el tipo de juego de caracteres adecuado para que reconozca los 
    acentos.
    Actualmente toma estos valores por defecto, sin embargo en versiones
    anteriores se requiere especificar el juego de caracteres a usar o de lo 
    contrario mostrará de forma no adecuada los caracteres especiales
"""
ruta_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"

archivo = open(ruta_archivo, 'r', encoding='utf8')
print(archivo.read())

archivo.close()
