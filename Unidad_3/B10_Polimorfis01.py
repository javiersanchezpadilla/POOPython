""" SOBRE ESCRITURA DE MÉTODOS EN PYTHON (OVERRIDE = ANULAR)

    El concepto de OVERRIDING tiene que ver con la extensión de 
    funcionalidades de un método definido en la superclase, esto es, 
    si lo llamamos desde la subclase pero dentro de un método que tiene 
    exactamente el mismo nombre que el método de la superclase, es algo 
    similar a la sobreescritura del método, sin embargo podemos agregar 
    más cosas antes o después de llamar al método original de la superclase 
    ver ejemplo01 y ejemlpo02 al final del documento, dónde se agregan textos 
    a los mostrados en el método original.

    Los términos sobrescribir y anular pueden parecer muy similares, pero en 
    realidad son bastante diferentes.
    Sobrescribir significa reemplazar código o datos existentes con código o 
    datos nuevos.
    Anular implica modificar el comportamiento de un método dentro de una 
    jerarquía. Cuando se anula un método, su nueva implementación tiene 
    prioridad sobre las implementaciones anteriores ubicadas más arriba en la 
    jerarquía.

    OVERRIDING:
    1) Prevalece sobre todas las cosas.
    2) Neutraliza la acción de
    3) Para extender o pasar por encima de

    En programación el concepto de sobreescritura es algo que usamos para 
    personalizar o extender la funcionalidad de un método que ya está definido 
    en la superclase

    Tomamos un método de la superclase y personalizamos o extendemos su 
    funcionalidad.
    Así podemos hacer que las instancias de nuestras subclases tengan 
    funcionalidad adicional en comparación con la superclase.
    Por ejemplo, si tenemos un método definido en la superclase y en la 
    subclase aquí tenemos la superclase y la subclase y vemos los métodos y 
    ambos tienen el mismo nombre.

    LLAMAR MÉTODOS DE UNA SUPERCLASE DESDE UNA SUBCLASE.
    ----------------------------------------------------

    SINTAXIS:
    Es importante notar que cuando usamos el nombre del la superclase debemos 
    indicar la palabra reservada “Self” como primer argumento.

    DENTRO DE LA SUBCLASE

                < SuperClase > . < method_name > (self, <argumentos>)

    Forma alternativa mediante el uso de la función super(), cuando hacemos uso 
    de esta función no se debe colocar la palabra reservada “Self”.

    DENTRO DE LA SUBCLASE

                super( )  . < method_name > ( <argumentos>)

    Aplicación:
                SuperClase
                def <method_name> ( self ):
                    pass

                subclase
                def  <method_name> (self)
                        <SuperClase> . < method_name > ( self)
"""

class Profesor:

    def __init__(self, nombre_completo, id_profesor):
        self.nombre_completo = nombre_completo
        self.id_profesor = id_profesor
        

    def bienvenidos_estudiantes(self):
        print(f"Bienvenidos a clase!! Soy su profesor, mi nombre es {self.nombre_completo}")


class ProfesorDeCiencias(Profesor):

    # def bienvenidos_estudiantes(self):
    #     print("Las ciencias son sorprendentes")
    #     # Vemos que el resto del código es igual al del método de la clase profesor
    #     print(f"Bienvenidos a clase!! Soy su profesor, mi nombre es {self.nombre_completo}")

    def bienvenidos_estudiantes(self):
        print("Las ciencias son sorprendentes")
        # Reemplazamos esta parte del código repetido y en su lugar llamamos al método
        # de la superclase
        Profesor.bienvenidos_estudiantes(self)  # Forma uno mediante el nombre de la superclase
        super().bienvenidos_estudiantes()       # mediante el uso de la funcion super()



mi_maestro_de_ciencias = ProfesorDeCiencias('Javier Sanhcez', '12345')
mi_maestro_de_ciencias.bienvenidos_estudiantes()
