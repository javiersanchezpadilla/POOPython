""" OPERADOR ID

    Cuando usamos el operador 'is' en realidad estamos preguntando si los
    elementos a comparar hacen referencia al mismo objeto en memoria.

        Sintaxis:
        objeto1 is objeto2

    Operador 'is' contra '=='
        a)  'is' verifica los objetos
        b)  == verifica los valores contenidos en los objetos

    Por lo anterior dos objetos pueden tener los mismos valores, pero aún
    así tener distintas direcciones de memoria.
"""

# En este ejemplo las dos variables hacen referencia al mismo objeto
# en la memoria
a = [1, 2, 3, 4, 5]
b = a

# Si afectamos cualquiera de las variables afectara al objeto original
# recordar que ambas apuntan a la misma dirección de memoria
b.append(10)
print(a)

print(a is b)

# Aqui se da un comportamiento muy interesante, ya que apesar de que son
# dos variables distintas, las cadenas son inmutables, por lo que pueden 
# compartir la misma dirección de memoria (ESTO ES PARA OPTIMIZAR MEMORIA)
x = "Hola a todos!!!"
y = "Hola a todos!!!"
print(x is y)

