""" Los Getters y Setters permiten set y get values

    Trabajando con GETTERs

    Digamos que es como obtener(get) y colocar o fijar (set) los 
    valores de los atributo de una instancia
    Ambos (get & set) proveen protección para los atributos de instancia
    proveyendo una forma indirecta para acceder o modificarlos, sirven
    como intermediarios.
    Incluso podemos tener atributos no publicos y aún así contar con
    una manera de poder acceder a ellos.
    Sintaxis:
                get_ + <atributo>            <objeto>.get_<atributo>
    
    Ejemplos con atributos específicos:
    get_nombre      get_edad        get_direccion       get_id
    get_color       get_x           get_y               get_vida

    LEEME:

    Los atributos públicos se pueden acceer directamente o incluso podemos usar
    getters y setters, pero al ser públicos tenemos la libertad de decidir, donde
    es obligatorio es cuando declaramos atributos no públicos, ahí si es necesario
    el uso de getters y setters
    
"""
class Pelicula:

    def __init__(self, titulo, rating):
        self._titulo = titulo       # Atributo no publico (debemos acceder con getters setters)
        self.rating = rating        # Atributo publico (podemos acceder directamente)

    def get_titulo(self):
        return self._titulo 
    

mi_pelicula = Pelicula('El padrino', 4.8)
print(mi_pelicula._titulo)      # Podemos acceder así lo cual es incorrecto
print('Mi pelicula favorita es', mi_pelicula.get_titulo())
print('El rating de la pelicula es ', mi_pelicula.rating)
