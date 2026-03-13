"""
    Maneras de ejecutar un método

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


    Recursión Infinita: Si dentro del setter de precio escriben 
    self.precio = new_precio en lugar de self.__precio = new_precio, el 
    programa entrará en un bucle infinito y se detendrá con un RecursionError. 
    Es el error más común al aprender @property.
    
                @property
                def precio(self):
                    return self._precio
                
                @precio.setter
                def precio(self, new_precio):
                    self._precio = new_precio
"""