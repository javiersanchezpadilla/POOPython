""" DECORADORES.

    Un decorador en Python es simplemente una función que recibe como entrada 
    otra función, le añade alguna funcionalidad extra sin modificar su código 
    original, y luego la devuelve modificada.

    Analogía: La funda de un teléfono inteligente
    ---------------------------------------------
    
    Imagina que tienes un teléfono celular común y corriente (esta es tu 
    función original). El teléfono hace lo que tiene que hacer: llamadas y 
    mensajes.
    Un día, decides comprarle una funda de uso rudo que además incluye una 
    batería extra y un soporte para mantenerlo parado (este es el decorador).
    No tuviste que abrir el teléfono ni soldar sus circuitos internos para 
    darle mas funcionalidades.
    Simplemente envolvimos el teléfono con la funda.
    Ahora, cuando usas el teléfono, sigue haciendo sus llamadas, pero además 
    tiene batería extendida y se sostiene solo. Lo decoraste.

    El secreto de Python: 
    ---------------------
    Las funciones son ciudadanos de primera clase.
    
    Antes de ver el código de un decorador, hay una regla de oro en Python
    las funciones se pueden tratar como si fueran variables. Esto significa 
    que puedes pasar una función como argumento dentro de otra función.
"""
def saludar():
    print("Hola")

                            # Guardamos la función dentro de otra variable 
                            # (¡sin usar paréntesis!)
mi_funcion = saludar 
mi_funcion()                # Salida: Hola
