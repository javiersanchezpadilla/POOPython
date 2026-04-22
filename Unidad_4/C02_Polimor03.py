""" POLIMORFISMO.

    Ejemplo aplicado a Pygame (Para tu laboratorio)
    Podemos manejar todos los elementos de su juego en un solo ciclo, sin 
    importar si son balas, naves o explosiones:

    ¿Por qué es fundamental?
    ------------------------

    1)  Escalabilidad: Puedes añadir nuevos tipos de objetos sin modificar 
        el motor principal del programa.
    2)  Abstracción: Te permite concentrarte en qué hace el objeto, no en 
        cómo lo hace.
    3)  Mantenimiento: Reduce drásticamente los bloques if/else o switch 
        gigantes que preguntan por el tipo de objeto.
"""

# Todos los elementos del juego tienen un método 'update'
elementos_juego = [jugador, enemigo1, enemigo2, bala_laser]

for item in elementos_juego:
    item.update() # Polimorfismo: cada uno se mueve a su manera

