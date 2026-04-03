""" HERENCIA. super() para referirse a la Superclase

    super() Esta es una función incorporada de Python que puede usar para hacer 
    referencia a la clase principal inmediata de la clase actual.

    'En una jerarquía de clases con herencia única, super() se puede usar para 
    referirse a clases principales sin nombrarlas explícitamente, lo que hace
    que el código sea más fácil de mantener. Este uso es muy paralelo al uso 
    de super() en otros lenguajes de programación'.


    Sintaxis alternativa:
    ---------------------
    Puedes usar super() en __init__() para hacer que tu subclase herede los 
    atributos de su superclase.

    Por ejemplo, aquí tenemos una subclase con la función super():

            Perro.__init__(self, nombre, edad)

            super().__init__(nombre, edad) 

    En la nueva sintaxis mediante el uso de super(), ya no es necesario pasar
    'self'

"""

class Perro:
 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
 
		
class Poodle(Perro):
 
    def __init__(self, nombre, edad, code):

        # Es quivalente a 
        # Perro.__init__(self, nombre, edad)
        super().__init__(nombre, edad)          
        self.code = code
