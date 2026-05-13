""" ESCRITURA DE ARCHIVOS DE TEXTO.

    writelines(list)
    ------------
    Escribir el contenido de una lista en un archivo de texto. 
    Resultado: HolaMundoEstaEsUnalista
"""

archivo = open("/home/javier/Documentos/Programas/Python/POOPython/datos.txt",'w')

lista = ['Hola','Mundo','Esta','Es','Una','lista']
archivo.writelines(lista)

archivo.close()
