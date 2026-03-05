""" DEFINICION DE GETTERS MEDIANTE DECORADORES.

    ¿Qué es un decorador?

    Un decorador es básicamente una función que toma una función como argumento
    y amplía su comportamiento sin modificarla explícitamente.
    Por eso lo llamamos decorador, es algo así cómo decorar otra función 
    ampliando su comportamiento, pero no modifica explícitamente la función, 
    sólo añade algo más de sabor o funcionalidad a la función.

    Crear un getter con decoradores sobre un atributo 'edad'.
    ---------------------------------------------------------

    @property                           <-- Definimos el decorador @property
    def edad(self):                     <-- 'edad' es el nombre_de_atributo
        return self._edad               <-- Retorna el atributo de instancia

    Crear un setter con decorador sobre un atributo 'edad'.
    -------------------------------------------------------

    @edad.setter                        <-- decorador setter @<atributo>.setter
    def edad(self, nueva_edad):         <-- 'edad' es el nombre_de_atributo 
        self._edad = nueva_edad         <-- Retorna el atributo de instancia
"""
class Movie:

    def __init__(self, titulo, valoracion):
        self.titulo = titulo
        self._valoracion = valoracion

    @property
    def valoracion(self):
        print("Estoy en el getter")
        return self._valoracion
    
    @valoracion.setter 
    def valoracion(self, nueva_valoracion):
        print("Estoy en el setter")
        if isinstance(nueva_valoracion, float):
            self._valoracion = nueva_valoracion
        else:
            print("Proporcione una edad valida")


mi_pelicula = Movie("Titanic", 4.3)
print(mi_pelicula.valoracion)
mi_pelicula.valoracion = 1.2
print(mi_pelicula.valoracion)
