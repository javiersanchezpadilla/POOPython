""" Los métodos son bloques de construcción fundamentales para las clases que
    escribimos en la programación orientada a objetos.
    Una clase define el estado y el comportamiento de un objeto.
    Al cubrir los métodos, estaremos aprendiendo como definir el comportamiento
    del objeto.
    Un método es una función asociada a un objeto de la clase o a la clase por 
    sí misma.
    Los métodos definidos en una clase determinan el comportamiento de los objetos
    creados de la clase y cómo ellos pueden interactuar con su estado.

    TIPOS DE MÉTODOS.

    **) Métodos de instancia. Son métodos que pertenecen a un objeto específico, 
        tienen acceso al estado del objeto que las llama
    **) Métodos de clase
    **) Métodos Estáticos.

    Básicamente estamos definiendo los comportamientos que un objeto puede tomar
    -----------------------------------------------------------------------------

    MÉTODOS DE INSTANCIA.
    ---------------------
    Los métodos de instancia. en particular son métodos que pertenecen a un objeto
    específico, Porque tienen acceso al estado del objeto que las llama.

    ¿Y cómo acceden estos métodos al estado interno del objeto? 
    Bueno, a través de self,  a través de este parámetro que hemos estado 
    escribiendo hasta ahora como el primer parámetro en cada uno de los métodos 
    que hemos definido en nuestra clase, como init, como getters y setters.

    Por ejemplo la clase list <class list> tiene metodos como append(), insert(), 
    remove(), sort(), etc.

    Sintaxis. Los nombres de los métodos usualmente incluyen nombres de verbos, 
    ya que representan una acción (caminar, sumar, restar, dividir, multiplicar, 
    correr), y se deben escribir en minúsculas con guiones entre las palabras 
    (snake-case).

    Sintaxis: 
                < objeto > . <method > ( < argumentos > )
    Ejemplo:

        class MyClass:

            # Class attributes
            def __init__():

            def method_name(self, param1, param2, … ) : 
                # code

    CADA INSTANCIA TIENE SU PROPIA COPIA DE CADA MÉTODO Y ESAS COPIAS SON 
    INDEPENDIENTES UNAS DE OTRAS ---> FALSO DE TODA FALSEDAD cada metodo de 
    instancia se refiere a los métodos definidos en la clase)

    Otra forma alternativa de llamar a los métodos es  (ver ej A10_MetodosInstancia06.py)

                <ClassName>.<method>(<instance>, <arguments>)
"""

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def encontrar_diametro(self):
        print(f'Diametro: {self.radio * 2}')


my_circle = Circulo(10)
my_circle.encontrar_diametro()
