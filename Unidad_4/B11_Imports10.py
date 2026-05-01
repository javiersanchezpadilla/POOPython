""" DEMOSTRACIÓN DE __all__ 

    En el código anterior se definiceron elementos públicos y privados

    Públicos
    
        def funcion_publica_1():
        class ClaseVisible:
        mi_variable_publica 
    
    Privados

        def funcion_privada_auxiliar():
        mi_variable_protegida 

__all__ = [ "funcion_publica_1", "ClaseVisible", "mi_variable_publica" ]

"""


from B11_Imports09 import *

funcion_publica_1()
a = ClaseVisible()
print(mi_variable_publica)

# funcion_privada_auxiliar()
# print(mi_variable_protegida)
