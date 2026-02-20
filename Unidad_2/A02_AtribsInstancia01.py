""" ¿QUÉ ES UNA INSTANCIA?

    Una instancia es simplemente un objeto creado a partir de una clase.
    A menudo estos dos términos se utilizan indistintamente, objeto e 
    instancia suele ser más teórico, y se refiere a un ejemplo particular de 
    una clase o de una definición teórica.
    Un objeto se utiliza normalmente para referirse a algo más concreto, el 
    objeto real que se almacena en la memoria.

    ATRIBUTOS DE INSTANCIAS.
    ------------------------
    En este caso, si tenemos un plano de mochila, crearíamos instancias u 
    objetos de mochila en nuestro código, las instancias tienen atributos y 
    estos atributos se denominan atributos de instancia.

    Son los atributos de un objeto. Son variables que pertenecen a un objeto 
    concreto.

    Así, una mochila puede tener, por ejemplo, un tamaño, un color, un peso, 
    un material, un número de bolsillos, un número de cremalleras o incluso 
    una lista de objetos que contiene.
    Todos ellos pueden ser atributos de instancia y describen las 
    características de la mochila y lo que contiene.

    Algo muy importante que debes saber:
    ------------------------------------ 
    Los atributos de instancia son independientes, pertenecen a los objetos. 

    Las clases se utilizan para definir los atributos como un plano, pero los 
    atributos pueden tener valores únicos para cada instancia.

    DEFINIR ATRIBUTOS DE INSTANCIA CON EL MÉTODO INIT.
    --------------------------------------------------

        __iint__( self )

    Vamos a comenzar con los elementos reales del cuerpo de una clase.
    El método especial __init__ ( self ) se usa para definir el estado inicial 
    de un objeto. Es llamado de forma automática cuando una instancia es creada
    y la razón es para inicializar los valores de los atributos de la instancia
    que se está creando.

    En este caso, definiremos un atributo de precio para las instancias de la Casa, 
    así, cada casa que creamos puede tener su atributo de precio con su propio 
    valor único e independiente.

    ERRORE COMUNES AL DECLARAR LAS CLASES CON SUS ATRIBUTOS DE INSTANCIA:
    --------------------------------------------------------------------
    A) Omitir la palabra 'def'  __init__ (self, peso, altura)    <-- Error
    B) Indicar solo un guion bajo al definir _init_     <-- Error
    C) Omitir la palabra 'self' como primer parametro  
            def __init__(peso, altura) <-- Error
    D) Omitir la palabra 'self' cuando definimos los atributos de clase
            def __init__(self, peso, altura):
                peso = peso
                altura = altura
    E) Buena practica es un espacio entre cada parametro después de la coma
            def __init__(self,peso,altura):     <-- Error 
"""


                            # Decidimos tomar el precio como argumento y usar ese
                            # valor que pasamos como argumento, y asignarlo al 
                            # atributo precio de la instancia. Esto es básicamente 
                            # lo que estamos haciendo aquí con esta línea, Self se 
                            # refiere al atributo de la instancia.  

class Casa:

    def __init__(self, precio):
        self.precio = precio


                            # Crear una clase sin elementos
class Mochila:

    def __init__(self):
        self.articulos = []




