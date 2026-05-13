""" AGREGAR INFORMACIÓN AL FINAL DEL ARCHIVO DE TEXTO.

    Utiliza el método writelines() para escribir los valores de una lista 
    al final del archivo de texto, después inserta un tabulador entre cada
    elemento de la lista para separarlos.
    Por último, imprime el contenido completo del archivo de texto.
    pista: recuerda que el simbolo para concatenar un tabulador es \t 
    también deberás cerrar el archivo en modo escritura y volverlo a abrir 
    en modo lectura para poder imprimir su contenido.

"""
archivo_ruta = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"
registro_ultima_sesion = ["Alberto", "12/05/2026", "19:34:32 hs", "Sin errores de carga"]

mi_archivo = open(archivo_ruta, 'a')
for palabraEnLista in registro_ultima_sesion:
    mi_archivo.writelines(palabraEnLista + '\t')

mi_archivo.close()

mi_archivo = open(archivo_ruta, 'r')
for l in mi_archivo:
    print(l.strip())

mi_archivo.close()
