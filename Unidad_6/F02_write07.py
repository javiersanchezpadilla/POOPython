""" MANEJO DE ARCHIVOS. 

    Creación y especificación del juego de caracteres para escribir acentos en 
    los archivos.

    En python podemos manejar archivos del tipo texto (txt) y archivos del tipo 
    binario (JPG,, doc, rar, csv, mp3, dll, xls, exe, html, png, etc)

    Ejemplo. Definición básica para crear o modificar un archivo existente, en 
    este caso no usar acentos o de lo contrario no se reconocerán los 
    caracteres con acentos y obtendremos un rror, si se ejecutará el contenido
    del archivo en la palabra información se veria así informaci�na
"""
nombre_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"

try:
    archivo = open(nombre_archivo,'w')
    archivo.write('Agregamos informacion')
    archivo.write('a nuestro archivo')
    archivo.write('como prueba\n')
    archivo.write('Esta es otra linea\n')
    archivo.write('y el final ...')
except Exception as e:
    print(e)
finally:
    archivo.close()
