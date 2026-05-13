""" USO DE WITH, ARCHIVOS Y CONTEXT MANAGER EN PYTHON

    El contexto WITH se ejecuta de forma automática y son dos métodos los que 
    se mandan a llamar.

    **) El método llamado __enter__() que es dónde se abre el archivo, así que 
        en este método es dónde se abre el recurso.
    **) El método llamado __exit__() que es el método encargado de cerrar el 
        archivo de forma automática.

    Sin embargo, nosotros podemos crear nuestra propia clase para el manejo de 
    estos recursos.
    Vamos a crear un nuevo método llamado ManejoArchivos.py y creamos nuestra 
    clase la cual no tiene que extender de ninguna otra clase ya que los 
    métodos requeridos están implícitos en la clase object y con esto ya lo 
    están heredando de la clase object directamente sin necesidad de 
    especificarlo, con el simple hecho de declarar la clase ya se encuentra 
    implícito.
    Sin embargo si tiene que implementar (sobreescribir) dos métodos el método
    __enter__() y el método __exit__() de la clase object (clase padre),

    Implementación en el archivo o módulo ManejoArchivod.py. Al momento de 
    invocar esta clase con with estaremos haciendo uso del Context Manager, 
    y de forma automática llamara cuando se requiera el método __enter__() y 
    posteriormente el método __exit__()
"""

archivo_ruta = "/home/javier/Documentos/Programas/Python/POOPython/datos.txt"

class ManejoArchivos:   
    def __init__(self, nombre):
        self.nombre = nombre        # recibimos el nombre del recurso en este 
                                    # caso el nombre del archivo

    def __enter__(self):            # Este metodo se hereda de la clase object
        print('Obtenemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre
    
                                    # Estos parámetros son obligatorios se 
                                    # usen o no
    def __exit__(self, tipo_exception, valor_excepcion, traza_error):
        print('Cerramos el recurso'.center(50,'-'))
        if self.nombre:     # Si este atributo aun apunta a un recurso lo cierra
            self.nombre.close()
