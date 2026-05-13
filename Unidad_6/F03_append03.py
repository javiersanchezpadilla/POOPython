""" AGREGAR INFORMACIÓN AL FINAL DEL ARCHIVO DE TEXTO.

    Abre el archivo de texto y añade una línea al final del mismo que diga 
    'nuevo inicio de sesión'. imprime el contenido completo del archivo de 
     texto al finalizar.

    pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo 
    lectura.
"""
archivo_ruta = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"

mi_archivo = open(archivo_ruta, 'a')
mi_archivo.write('Nuevo inicio de sesión')
mi_archivo.close()

mi_archivo = open(archivo_ruta, 'r')
for l in mi_archivo:
    print(l.strip())


mi_archivo.close()
