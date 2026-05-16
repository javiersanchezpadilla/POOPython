""" ESCRITURA DE ARCHIVOS DE TEXTO


        mi_archivo = open ('archivo.txt', 'modo')

    Dónde modo puede ser
    --------------------
    r	Solo lectura, podemos indicarlo u omitirlo, en ambos casos es lectura.
    w	Modo escritura, sobreescribe el contenido de un archivo (lo reemplaza)
    a	Si no existe lo crea y si existe agrega información al final del mismo

    Para los ejemplos seguiré trabajando con el archivo de texto.

    Debemos entender y ser coherentes entre la forma de abrir un archivo y las
    operaciones a realizar con el mismo archivo.
    para entender esto abriré un archivo en modo de solo lectura e intentare 
    escribir algo dentro del mismo, lo cual es incorrecto porque el modo solo 
    lectura no permite otra operación que no sea solo leer.

    ESTE CÓDIGO MARCA ERROR, solo es para mostrar que se debe respetar cada
    modo de acceso a los archivos.
"""

archivo = open("/home/javier/Documentos/Programas/Python/POOPython/datos.txt",'r')
archivo.write('Linea a escribir')   # no podemos escribir en modo lectura

archivo.close()
