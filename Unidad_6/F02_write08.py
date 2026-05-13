""" MANEJO DE ARCHIVOS. 

    ESPECIFICAR EL JUEGO DE CARACTERES A UN ARCHIVO DE TEXTO.
    ---------------------------------------------------------
    Ya vimos que no podemos usar acentos en las palabras o de lo contrario no 
    se reconocerán dentro del archivo de texto, para corregir esto definimos 
    el juego de caracteres a usar al momento de abrir el archivo, de esta 
    forma se reconocerán los acentos.
"""
nombre_archivo = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"

try:
    archivo = open(nombre_archivo,'w', encoding='utf8')
    archivo.write('Agregaré información')
    archivo.write('a nuestro archivo')
    archivo.write('usando acentos')
    archivo.write('en palabras como máximo\n')
    archivo.write('mínimo, estación, educación, tecnológico\n')
    archivo.write('Esta es otra linea\n')
    archivo.write('y el final ...')
except Exception as e:
    print(e)
finally:
    archivo.close()
