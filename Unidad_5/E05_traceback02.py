""" TRACEBACK

    EN LOS SIGUIENTES EJEMPLOS SE COMETERAN ERRORES PARA PODER EXPLICAR 
    EL CONCEPTO DE TRACEBACK

    Error dentro de una función anidada
    Así queda el traceback
    Traceback (most recent call last):
    File "/home/javier/...../E05_traceback02.py", line 23, in <module>
    nivel1()
    File "/home/javier/...../E05_traceback02.py", line 20, in nivel1
    return nivel2()
           ^^^^^^^^
    File "/home/javier/...../E05_traceback02.py", line 16, in nivel2
    return nivel3()
           ^^^^^^^^
    File "/home/javier/...../E05_traceback02.py", line 12, in nivel3
    return 10 / 0
           ~~~^~~
    ZeroDivisionError: division by zero
    
    Analogía: 
    ---------
    Es como una llamada en cadena: Juan le dijo a María, María le dijo a Pedro, 
    Pedro le dijo a Luis, y Luis cometió el error.
"""
            # Esta función es la que contiene el error
def nivel3():
    return 10 / 0

            # Esta función llama a  funcion nivel 3
def nivel2():
    return nivel3()

            # Esta función llama a  funcion nivel 2
def nivel1():
    return nivel2()

            # Llamamos a la funcion nivel 1
nivel1()