""" MANEJO DE ARCHIVOS. 

     Leer y copiar el contenido de un archivo en otro. 
"""
dir_archivo1 = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"
dir_archivo2 = "/home/javier/Documentos/Programas/Python/POOPython/datos2.txt"

archivo = open(dir_archivo1,'r', encoding='utf8')
archivo2 = open(dir_archivo2,'a', encoding='utf8')

archivo2.write(archivo.read())

archivo.close()
archivo2.close()
