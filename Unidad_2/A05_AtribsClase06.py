""" MECANISMO DE BUSQUEDA DE ATRIBUTOS

    La forma correcta de acceder a los atributos de clae es indicando

        NombreClase.atributo_de_clase       (NaveEnemiga.max_mov)

    Pero, ¿qué pasa si intentamos buscarlo como si fuera un atributo de 
    instancia?

        objeto.atributo_de_clase            (n1.max_mov  o  n1.min_mov)

        
    1. ¿Cómo busca Python los atributos?
    ------------------------------------
    Cuando tú escribes n1.max_mov, Python no se rinde si no encuentra 
    max_mov dentro del objeto n1. Sigue un orden de búsqueda muy específico:

    1) Primero busca en la Instancia (el objeto): ¿Tiene el objeto n1 un atributo
       llamado max_mov en su propio espacio de memoria (su __init__)? 
       Respuesta: No.

    2) Segundo busca en la Clase: Como no lo encontró en el objeto, Python sube un 
       nivel y pregunta: "¿Tiene la clase Nave un atributo llamado max_mov?". 
       Respuesta: Sí.

    Como lo encontró en la clase, Python te lo entrega. Por eso parece que el objeto 
    "tiene" el atributo, pero en realidad lo está "tomando prestado" de su clase.

    2. ¿Se convierte en un atributo de instancia?
    ---------------------------------------------
    No. El atributo sigue perteneciendo a la clase. El objeto simplemente tiene acceso 
    a él para leerlo.
    Es como si la clase fuera una "biblioteca" y los objetos fueran los "usuarios". 
    Los usuarios pueden leer los libros de la biblioteca (n1.max_mov), pero el libro 
    sigue estando en la biblioteca, no en la casa de cada usuario.

    3. El peligro: Lectura vs. Escritura (¡Mucho ojo aquí!)
    -------------------------------------------------------
    Aquí es donde la mayoría de los programadores se confunden. El comportamiento cambia 
    totalmente si intentas modificarlo:

    *) Si solo lees: print(n1.max_mov) -> Python busca en la clase y te da el 10.
    *) Si intentas cambiarlo desde el objeto: 
            n1.max_mov = 20  ¡Cuidado!

       Aquí, Python NO CAMBIA el atributo de la clase. Lo que hace es crear un 
       NUEVO ATRIBUTO DE INSTANCIA llamado `max_mov` solo para `n1`.
"""

import random

class NaveEnemiga:

    min_mov = 1
    max_mov = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y


n1 = NaveEnemiga(0, 0)
n2 = NaveEnemiga(10, 0)
print(n1.x,n1.y)

# Imprimimos los atributos de clase
# Está es la forma correcta de acceder a los atributos de clase
print(f'Movs nave desde Clase Min = {NaveEnemiga.min_mov}, Max = {NaveEnemiga.max_mov}')


# Cuando tú escribes n1.max_mov, Python no se rinde si no encuentra 
# max_mov dentro del objeto n1. Sigue un orden de búsqueda muy específico:
# 1) Primero busca en la Instancia (el objeto): ¿Tiene el objeto n1 un atributo
#    llamado max_mov en su propio espacio de memoria (su __init__)? 
#    Respuesta: No.
# 2) Segundo busca en la Clase: Como no lo encontró en el objeto, Python sube un 
#    nivel y pregunta: "¿Tiene la clase Nave un atributo llamado max_mov?". 
#    Respuesta: Sí.
# Como lo encontró en la clase, Python te lo entrega. Por eso parece que el objeto 
# "tiene" el atributo, pero en realidad lo está "tomando prestado" de su clase.
#
# 2. ¿Se convierte en un atributo de instancia? No. El atributo sigue perteneciendo
#     a la clase. El objeto simplemente tiene acceso a él para leerlo.
print(f'Movs nave desde objeto Min = {n1.min_mov}, Max = {n1.max_mov}')


# CUIDADO!!!!! ¿Qué pasa cuando lo intentamos modificar
# Aquí, Python NO CAMBIA el atributo de la clase. Lo que hace es crear un 
# NUEVO ATRIBUTO DE INSTANCIA llamado `max_mov` solo para `n1`.
n1.min_mov = 100
n1.max_mov = 1000
print('\nSe modifico mediante n1.min_mov=100 y n1.max_mov=1000')
print(f'Movs nave desde Clase Min = {NaveEnemiga.min_mov}, Max = {NaveEnemiga.max_mov}')
print(f'Movs nave desde objeto n1 Min = {n1.min_mov}, Max = {n1.max_mov}')

print('\nMostramos los atributos desde otro objeto')
print(f'Movs nave desde objeto n2 Min = {n2.min_mov}, Max = {n2.max_mov}')

print('\nInventario del objeto n1:')
print(n1.__dict__)

print('\nInventario del objeto n2:')
print(n2.__dict__)

# aqui vamos a ver min_mov = 1 y max_mov = 10
print('\nInventario de la clase')
print(NaveEnemiga.__dict__)

# De nuevo el inventario de la nave pero mas simplificado
print("\n--- Inventario de la Clase Nave ---")
# Filtramos un poco para no ver cosas raras de Python
print({k: v for k, v in NaveEnemiga.__dict__.items() if not k.startswith('__')})
