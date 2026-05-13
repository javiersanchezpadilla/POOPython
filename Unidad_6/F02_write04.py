""" ESCRITURA DE ARCHIVOS DE TEXTO.

    Insertar líneas o enters entre línea y línea forma 2 usando el caracter de 
    edicion de triple comilla e insertar el enter entre línea y linea
"""

archivo = open("/home/javier/Documentos/Programas/Python/POOPython/datos.txt",'w')

archivo.write('''Linea 1
Linea 2
Linea tres''')

archivo.close()
