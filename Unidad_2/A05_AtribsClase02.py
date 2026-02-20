""" DEFINICIÓN DE LOS ATRIBUTOS DE CLASE.

    Los atributos de clase pertenecen a una clase y no a una instancia 
    concreta.
    Todas las instancias de la clase tienen acceso a este atributo.
    Ellos comparten el mismo valor, así que cualquier cambio a este valor 
    afecta a todas las instancias.
    Todos ellos comparten el mismo valor, así que cualquier cambio realizado 
    a este valor afectará a todas las instancias.

            class ClassName:
	            # Atributos de clase
	            def __init__ (self):
	            # Métodos

*) Los atributos de clase pertenecen a la clase.
*) Son compartidos por todas las instancias de la clase.
*) Los atributos de clase se pueden utilizar para definir constantes a nivel 
   de clase o valores predeterminados que debe compartirse entre todas las instancias.

"""

class PersonajeJuego:
    # Definicion de los atributos de clase    
    SALUD_POR_DEFECTO = 100

    # Definición de los atributos de instancia
    def __init__(self, tipo_caracter):
        self.tipo_caracter = tipo_caracter
        self.salud = PersonajeJuego.SALUD_POR_DEFECTO


a = PersonajeJuego('Mago')
print('Tipo de caracter:', a.tipo_caracter, 'Nivel de vida:', a.salud)
