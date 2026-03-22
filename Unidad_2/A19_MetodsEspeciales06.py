""" MÉTODO __add__( ).

    object.__add__ (self, other)
    Se pueden definir los siguientes métodos para emular objetos numéricos.
    Los métodos correspondientes a operaciones no soportadas por el tipo 
    concreto de número implementado deben dejarse sin definir.
    Aquí podemos ver que este método toma dos parámetros self y other, 
    los dos operandos que intervendrán en la operación.
                x + y  	------>   x.__add__(y)

    Ejemplo, evaluar la expresión 'X' más 'Y', donde 'X' es una instancia 
    de una clase que tiene definido un método __add__(), entonces esto es 
    lo que realmente se llama entre bastidores.
    El método __add__(), se ejecuta entre bastidores, esta es la parte que 
    nos interesa ahora, cómo vamos a personalizar el comportamiento del 
    operador.
    Cuando se ejecuta el operador '+' indirectamente se manda a llamar el 
    método __add__( )
"""
print(3 + 4)
print((3).__add__(4))

print("Hola " + "Mundo!!!")
print(("Hola ").__add__("Mundo!!!"))

print([1, 2, 3] + [4, 5, 6, 7])
print(([1, 2, 3]).__add__([4, 5, 6, 7]))


