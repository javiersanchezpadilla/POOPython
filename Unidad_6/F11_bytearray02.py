""" BYTEARRAY

    El secreto: Por dentro solo hay números enteros
    -----------------------------------------------
    Aunque en la consola veas que dice b'HOLA', Python por dentro no está 
    guardando las letras como tal. Está guardando sus valores numéricos 
    correspondientes en el código ASCII (el mapa universal que le dice a la 
    computadora qué número le toca a cada letra).

    Si usamos un ciclo for para ver qué hay dentro de nuestro bytearray, 
    descubriremos los números ocultos:

    72   # (Este número representa a la 'H')
    79   # (Este número representa a la 'O')
    76   # (Este número representa a la 'L')
    65   # (Este número representa a la 'A')

"""

letrero = bytearray("HOLA", "utf-8")

for numero in letrero:
    print(numero)