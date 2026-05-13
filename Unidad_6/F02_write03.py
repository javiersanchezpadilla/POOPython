""" ESCRITURA DE ARCHIVOS DE TEXTO.

    Insertar líneas o enters entre línea y línea forma 1 usando el caracter de 
    salto de línea '\n'
"""

archivo = open("/home/javier/Documentos/Programas/Python/POOPython/datos.txt",'w')

archivo.write('Linea 1\n')
archivo.write('Linea 2\n')
archivo.write('Linea 3\n')
archivo.write('Linea 4\n')

archivo.close()
