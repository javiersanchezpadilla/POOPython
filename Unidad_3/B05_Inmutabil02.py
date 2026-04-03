""" MUTABILIDAD INMUTABILIDAD.

    Ventajas y desventajas del uso de objetos mutables e inmutables:
    ----------------------------------------------------------------

    OBJETOS MUTABLES:

    1) VENTAJAS:    Poder reusar objetos existentes en lugar de tener que 
                    realizar nuevas copias para cada cambio.
    2) DESVENTAJAS: El uso de objetos mutables en un programa puede 
                    introducir errores (bugs), porque podrias de forma
                    involuntaria mutar un objeto en el programa.

    Potencial riesgo usando Aliasing.
    ---------------------------------
    Aquí podemos mutar un objeto de forma no intencional a traves de un alias
    ya que al reasignar un objeto mutable a una variable y esta a su vez a 
    otra mas podemos pensar que estamos creando una copia, cuando en realidad
    estamos forzando a apuntar a la misma dirección de memoria del mismo
    objeto (aliasing), por lo tanto los cambios realizados en una variable u
    otra afectaran al mismisimo objeto (ya que son la misma referencia)
"""                    

a = [1, 2, 3, 4]
b = a               # Aqui podemos pensar que estamos obteniendo una copia

b.append(10)        # Afectamos a la variable 'b' pero en realidad es la 
b.append(11)        # misma referencia al mismo objeto, ya que 'a' y 'b' 
b.append(12)        # son el mismo objeto en memoria

print(a)
