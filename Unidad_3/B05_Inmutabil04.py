""" MUTABILIDAD INMUTABILIDAD.

    Ventajas y desventajas del uso de objetos mutables e inmutables:
    ----------------------------------------------------------------

    OBJETOS INMUTABLES:
    -------------------

    1) VENTAJAS:    **) Al no poder modificarse es menor probable que 
                        introduzcan errores en el programa.
                    **) También pueden ser mas faciles de entender porque 
                        conocemos su valor exacto sin cambios ocultos u 
                        objetos que nunca deben cambiar en el programa
                        inesperados.
                    **) Son faciles de entender, en todo momento se conoce
                        su valor exacto sin la posibilidad de un cambio 
                        inesperado.
    2) DESVENTAJAS: **) Son menos eficientes en terminos del uso de la 
                        memoria, el costo para modifcarlos es alto ya que es
                        necesario crear una nueva del objeto para poder 
                        realizar cualquier cambio

    En el siguiente ejemplo se requiere insertar el valor 7 en la sigueinte 
    tupla entre el valor 2 y el 3, el resutlado va a ser un nuevo objeto 
    del tipo tupla el cual tendrá una nueva dirección de memoria.
"""  

a = (1, 2, 3, 4)
print(a)
print(id(a))

                        # se tiene que crear un nuevo objeto para poder 
                        # lograr el cambio
a = a[:2] + (7,) + a[2:]
print(a)                # podemos ver que las direcciones de memoria 
print(id(a))            # son distintas
