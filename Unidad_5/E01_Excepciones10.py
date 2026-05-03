""" CREACIÓN DE CLASE DE EXCEPCIÓN PERSONALIZADA.

    Recordemos que tenemos una serie de clases definidas para el manejo de las 
    excepciones, aunque podemos manejar de forma específica los errores, lo 
    común es trabajarlos desde la clase Exception, también podríamos trabajar 
    desde la clase BaseException, pero como se mencionó lo común es trabajar a 
    partir de la clase Exception. 

                                   +<-- AritmeticError <---- ZerodivisionError
                                   |
                                   |                    |<-- FileNotFoundError
                                   +<-- OSError --------+
                                   |                    |<-- PermissionError
                                   |
    BaseException <-- Exception <--+<-- RuntimeError
                                   |                    |<-- IndexError
                                   +<-- LoopUpError <---+
                                   |                    |<-- KeyError
                                   |
                                   +<-- SintaxError <------- IndentationError  

    Sin embargo también podemos manejar nuestras excepciones de forma 
    personalizada, vamos a suponer que quiero crear una excepción para la 
    captura de dos números identicos, lo cual no es algo valido pero para modo 
    de aprendizaje nos permitira enternder el concepto.
    Creamos un módulo llamado 
    
            NumerosIdenticosException.py  

    Nuestra clase para el manejo de errores va a extenderse a la clase 
    Excepción (va a heredar de la clase exception), como podemos ver en la 
    clase creada primero de le asignamos un nombre y la extendemos de la clase
    padre Exception, recibimos como parámetro un mensaje personalizado que 
    nosotros asignaremos y lo asignaremos al atributo message de la clase 
    padre Exception. 

    Creamos el modulo NumerosIdenticosException.py
    ----------------------------------------------

            class NumerosIdenticosException(Exception):

            def __init__(self, mensajito):
                self.message = mensajito

    Ahora regresamos a nuestro programa principal y para poder utilizarla 
    tenemos que importarla, así como validamos el error, para lanzar la 
    excepcion tenemos que usar la palabra reservada raise con la clase creada 
    y el mensaje, recordemos que nuestra clase creada pertenece a la clase 
    padre Exception por lo que a partir de este momento se procesa el bloque 
    (except Exception as e:).

    EN MI CASO EL NOMBRE DEL MÓDULO ES E01_Excepticiones10.py
"""
class NumerosIdenticosException(Exception):

    def __init__(self, mensajito):
        self.message = mensajito
        # Aquí podemos dar tratamiento el error