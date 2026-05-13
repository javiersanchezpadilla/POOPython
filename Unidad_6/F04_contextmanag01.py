""" USO DE WITH, ARCHIVOS Y CONTEXT MANAGER EN PYTHON

    Hasta ahora para hacer uso de un archivo primero tenemos que abrirlo 
    (open) y al final debemos cerrarlo (close), en caso de no hacerlo al 
    finalizar el programa Python lo cierra por nosotros de forma automática, 
    sin embargo se recomienda hacer esta operación, además también es 
    recomendable realizar estas operaciones a través de un bloque para el 
    manejo de las excepciones (try - except) de una forma eficiente.

            try:
                archivo = open('Prueba.txt','w', encoding='utf8')   <<<<<<
                archivo.write('Agregaré información')
                archivo.write('a nuestro archivo')
                archivo.write('como prueba\n')
                archivo.write('Esta es otra linea\n')
                archivo.write('y el final ...')
            except Exception as e:
                print(e)
            finally:
                archivo.close()                                     <<<<<<<
    
    Sin embargo existe una manera simplificada y de forma automática va a 
    cerrar nuestro archivo, para manejar esto, a esto se le conoce como el 
    manejo de contexto WITH.
    La gran ventaja es que al usar el contexto WITH  de forma automática abre 
    el archivo y cierra el archivo, esto se conoce como CONTEXT MANAGER o 
    administrador de recursos.
"""
archivo_ruta = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"

with open(archivo_ruta,'r', encoding='utf8') as archivo:
    print(archivo.read())

