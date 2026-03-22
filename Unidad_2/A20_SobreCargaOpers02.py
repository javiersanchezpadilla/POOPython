""" MÉTODO __GETITEM___

    object. __getitem__(self, key)

    Llamado a implementar evaluaciones de self[clave]. Para los tipos de 
    secuencia, las claves aceptadas deben ser números enteros y objetos 
    slicing.
    Tener en cuenta que la interpretación especial de los índices negativos 
    (si la clase desea emular un tipo de secuencia) depende del método 
    __getitem__(). Si la clave es de un tipo inadecuado, se puede generar 
    TypeError; si se trata de un valor fuera del conjunto de índices de la 
    secuencia (después de cualquier interpretación especial de valores 
    negativos), se debe generar IndexError. Para tipos de mapeo, si
    Falta la clave (no está en el contenedor), se debe generar KeyError.

    Nota: los bucles 'for' esperan que se genere un IndexError para índices 
    ilegales para permitir la detección adecuada del final del secuencia.

        objeto [ index ]  ---->   __getitem__ ( )
"""

mi_lista = ["a", "b", "c", "d"]
mi_cadena = "Hola"

print(mi_lista[0])
print(mi_lista[1])
print(mi_lista[2])
print(mi_lista[3])

# __getitem__ se encarga de extraer el elemento de acuerdo a su posición
print('--------')
print(mi_lista.__getitem__(0))
print(mi_lista.__getitem__(1))
print(mi_lista.__getitem__(2))
print(mi_lista.__getitem__(3))

# para la cadena
print('--------')
print(mi_cadena[0])
print(mi_cadena[1])
print(mi_cadena[2])
print(mi_cadena[3])

# __getitem__ se encarga de extraer el elemento de acuerdo a su posición
print('--------')
print(mi_cadena.__getitem__(0))
print(mi_cadena.__getitem__(1))
print(mi_cadena.__getitem__(2))
print(mi_cadena.__getitem__(3))
