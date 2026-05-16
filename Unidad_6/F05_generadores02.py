""" GENEADORES (YIELD)

    Pero qué sucede si excedemos el número válido de llamadas que podemos 
    hacer al generador?

    Resultado. Como no existe un cuarto valor para producir nos indica un 
    error. No podemos consumir más valores de los que produce la función 
    generadora manda un error de stop generation.

        Traceback (most recent call last):
        File "C:/Cursos/.../Generadores.py", line 12, in <module>
            print(next(gen))
        StopIteration
"""
def generador():
    yield 1
    yield 2
    yield 3             # El máximo de valores que podemos producir es 3

gen = generador()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))        # No existe un cuarto valor para producir ERROR!!!


