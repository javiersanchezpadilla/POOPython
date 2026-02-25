""" ATRIBUTOS DE CLASE VS ATRIBUTOS DE INSTANCIA.

    Repasemos las diferencias entre los atributos de clase y los atributos de
    instancia.


    ATRIBUTOS DE CLASE
    ------------------
    1) Pertenecen a la clase misma.
    2) Cambiando su valor afectará todas las instancias de la clase, porque 
       todas las instancias toman el valor de la misma fuente (la misma clase)

    ATRIBUTOS DE INSTANCIA.
    -----------------------
    1) Pertenecen a las instancias.
    2) Cada instancia tiene sus propios, independientes copia de los atributos.
    3) Cambiando su valor afectará solamente a las instancias particulares, 
       las otras instancias no serán afectadas.


    CUANDO USAR ATRIBUTOS DE CLASE.
    -------------------------------
    Los atributos de clase son de ayuda cuando necesitamos compartir un valor 
    entre todas las instancias de una clase.

    En el siguiente ejemplo contaremos las instancias de clase creadas
    Cuando se crea e inicializa una nueva instancia, el valor actual de 
    cliente_id se asigna a la id de la instancia y luego se incrementa en 1,
    por lo que la siguiente instancia tendrá la identificación actualizada.
"""

class Cliente:

    cliente_id = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Cliente.cliente_id += 1 
        self.id = Cliente.cliente_id 
        

c1 = Cliente('Juan')
c2 = Cliente('Pedro')
c3 = Cliente('Karla')

print(c1.id, c1.nombre)
print(c2.id, c2.nombre)
print(c3.id, c3.nombre)

print('Total de instancias creadas:', Cliente.cliente_id)
print('Total de instancias creadas:', c1.cliente_id)
print('Total de instancias creadas:', c2.cliente_id)
print('Total de instancias creadas:', c3.cliente_id)

# Como el atributo de clase es compartido con todas las instancias
# al momento de ser modificado cambiará para todos los objetos.
Cliente.cliente_id = 100
c4 = Cliente('Susana')
print(c4.id, c4.nombre)

print('Total de instancias creadas:', Cliente.cliente_id)
print('Total de instancias creadas:', c1.cliente_id)
print('Total de instancias creadas:', c2.cliente_id)
print('Total de instancias creadas:', c3.cliente_id)
