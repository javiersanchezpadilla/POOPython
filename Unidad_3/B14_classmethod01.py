""" MÉTODOS DE CLASE.

    Un método estático no recibe información de la clase en sí misma, por lo 
    que no tiene información directamente de nuestra clase, pero sirve para 
    asociar de manera lógica algún método que no tenga que ver con los 
    atributos de nuestra clase, no reciben ningún tipo de información.
    Un método estático no recibe ninguna referencia de nuestra clase y por lo 
    tanto no contiene ninguna información de nuestra clase, por lo tanto para 
    poder usar las variables de la clase se requiere hacer referencia a la clase.

        @staticmethod
        def metodo_estatico( ): 	        ← No recibe info de nuestra clase	
            print(MiClase.variable_clase)	← requiere hacer referen a la clase

    Un método de clase si recibe un contexto de clase, el parámetro CLS (class) 
    es una referencia para la clase misma y de igual forma que self y el 
    contexto dinámico nos permite acceder a los atributos de la instancia el 
    argumento CLS nos permite acceder a las variables de clase.
    Los métodos de clase podemos ver que si reciben información de la clase en 
    sí misma y con este valor podemos acceder a las variables de clase o 
    métodos de clase.

            @classmethod
            def metodo_clase(cls):
                print(cls.variable_clase)
"""
class MiClase:
    variable_clase = 'Valor variable'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():              # Un método estatico no recibe nunguna
        print(MiClase.variable_clase)	# referencia de nuestra clase

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

MiClase.metodo_clase()

