""" ¿Qué es el valor self? 

    ESTE EJEMPLO PERMITE ENTENDER COMO FUNCIONA. realmente 'self'
    apunta a cada dirección de memoria de cada objeto, el siguiente
    programa (el que sigue despues de este muesrta con mas objetos)

    La salida estándar que verá cuando imprima una instancia.
    Puede ver que se trata de una instancia de Casa ubicada en 
    ese lugar particular de la memoria (0x032AE0B8).

    Por tanto, self tiene un valor, una referencia al nuevo objeto.
    Increíble, ¿verdad? Así es como funciona el proceso entre bastidores.

    En este ejemplo imprimios el valor de 'self' que realmente apunta a la
    dirección de memoria del objeto, lo cual podemos comprobar si solicitamos
    la impresion del ID() del objeto convertido a Hexadecimal hex(id(Objeto))
"""

class Casa:

    def __init__(self, precio):
        print(self)                 # aqui vemos que 'self' apunta a la DIR
        self.precio = precio
        


mi_casa = Casa(1000)        
                                    # Imprime la direccion de memoria
print('mi_Casa', hex(id(mi_casa)))  # del objeto
