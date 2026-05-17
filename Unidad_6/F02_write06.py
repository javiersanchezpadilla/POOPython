""" ESCRITURA DE ARCHIVOS DE TEXTO.

    Escribir el contenido de una lista respetando una línea por palabra, 
    mediante el uso de un ciclo e inserción de nueva línea '\n'
"""

archivo = open("/home/javier/Documentos/Programas/Python/POOPython/datos.txt",'w')

lista = ['Hola','Mundo','Esta','Es','Una','lista']

for palabraEnLista in lista:
    archivo.writelines(palabraEnLista + '\n')

archivo.close()
