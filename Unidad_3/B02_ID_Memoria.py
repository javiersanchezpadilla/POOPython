""" Caa objeto declarado ocupa una dirección de memoria

    Podemos identificar estas direcciones mediante ID

    self realmente es el restreo que hace cada programa para referiste
    a la dirección de memoria del objeto creado

    Existe una diferencia muy sutil entre un objeto y una instancia. 
    En la mayoría de los casos, verá que se usan indistintamente.

    Un objeto es una representación conceptual de una entidad, mientras 
    que una instancia es la implementación real de esta entidad en el programa.
    Por ejemplo, un objeto Casa es la representación conceptual de una casa en 
    código, mientras que una instancia de casa es la implementación real de una
    casa.
"""
a = 5

# ID() retorna la dirección de un objeto en la memoria
print(id(a))
print(hex(id(a)))

print(id(15))
print(id("Hola a todos"))
print(id([1, 2, 3, 4, 5]))

