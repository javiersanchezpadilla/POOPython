""" RESULTADOS INESPERADOS PARA IS

    Python para ahorrar memoria rompe la regla de nuevas asignaciones de 
    memoria para nuevas variables, sobre todo en objetos que son inmutables

    Para enteros pequeños entre -5 y 256 asigna la misma dirección de memoria
    basicamente los valores entre -5 y 256 ya estan asignados en memoria, así
    que por eso los referencia a la misma dirección hasta que son modificados
"""

x = "Hola a todos!!!"
y = "Hola a todos!!!"
print("Para las cadenas", x is y)

a = 355
b = 355
print("PAra los valores numéricos", a is b)

print('\nVerificar las direcciones de memoria')
c = 'Hola'
print(id(c))        # En todos estos casos veremos que aunque sean distintas
d = 'Hola'          # variables al ser el texto un objeto inmutable, para 
print(id(d))        # ahorrar memoria leas asigna la misma dirección de memoria
e = 'Hola'
print(id(e))
f = 'Hola'
print(id(f))
g = 'Hola'
print(id(g))

# verificamos todos de un solo jalon
print('Validando todas los objetos', c is d is e is f is g)
