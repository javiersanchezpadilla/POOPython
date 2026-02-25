""" Atributos no públicos (Non-Public attribute)

    Es un atributo que no deberá se accedido o moficidado desde
    afuera de la clase.
    En Python no existe el terminó Atributi privado, por eso
    es no público.

                +-- Por convencion  -------------->  _<atributo>
                |
    Non Public  |
                |
                |   Cambiando el nombre
                +-- (lo hace un poco mas
                    dificil de acceder) ----------> __<atributo>
                    NAME MANGLING                Solo para casos especiales

                    
    Se entiende que cuando un programador ve dentro del código que uno de los
    atributos tiene un guión bajo, significa que no debe cambiar su valor 
    (aunque si es posible), por otro lado existe el cambio de nombre usando 
    doble guión bajo, sin embargo esta segunda opción solo debe usarse en casos 
    especiales.

    ¿por qué seguimos utilizando el término público en lugar de privado?
    -------------------------------------------------------------------- 
    si ya has aprendido a trabajar con otros lenguajes de programación como Java, 
    verá comúnmente el término privado. Pero aquí estamos utilizando el término 
    no público.
    En Python, no usamos el término privado, ya que ningún atributo es realmente 
    privado en Python.
                
"""

# Voy en el apunto C01_Encapsulamiento leccion de estefania 58