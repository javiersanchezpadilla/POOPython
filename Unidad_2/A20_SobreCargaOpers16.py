""" Pertenencia de Elementos (__contains__)

    Este es muy elegante. Permite usar la palabra clave in para saber si algo 
    está 'dentro' de tu objeto. Imagina una Playlist.

    Operador    Método              Uso común en el aula
    ==          __eq__          Comparar si dos alumnos o productos son 
                                'el mismo'
    +           __add__         Combinar carritos de compra o unir piezas de 
                                un robot.
    in          __contains__    Buscar un ingrediente en una receta o un alumno 
                                en una lista.
    len()       __len__         Saber cuántos objetos hay dentro de un contenedor

"""
class Playlist:
    def __init__(self, canciones):
        self.canciones = canciones

    # Sobrecarga del operador 'in'
    def __contains__(self, cancion_buscada):
        return cancion_buscada in self.canciones

# Uso
mi_mix = Playlist(["La Nave del Olvido", "Triste", "El Amar y el Querer"])

if "Triste" in mi_mix: # Esto llama internamente a __contains__
    print("¡Esa canción está en la lista!")
