""" El método "Formateador" (Nivel Presentación)

    Este es muy común cuando queremos que el resultado final tenga un 
    diseño específico. El método obtener_informacion llama a otro que 
    limpia los datos.

    Puntos clave:
    -------------
    **) El puente self: Sin el self., Python buscará una función fuera de la clase 
        y lanzará un error porque no encontrará el método.
    **) Modularidad: Es mejor tener 5 métodos pequeños que hacen una sola cosa bien, 
        que un método gigante que hace todo.
    **) Privacidad: Nota que en los ejemplos 1 y 3 usé el doble guion bajo (__). 
        Esto es porque esos métodos son "ayudantes" y no queremos que el usuario los 
        llame desde afuera; solo la clase debe usarlos.
    
    """

class Robot:
    def __init__(self, nombre, version):
        self.nombre = nombre
        self.version = version

    def __formatear_texto(self, texto):
        """Convierte cualquier texto a mayúsculas y le pone bordes."""
        return f"*** {texto.upper()} ***"

    def mostrar_identidad(self):
        # Llamamos al formateador para el nombre y la versión
        info = f"{self.nombre} v{self.version}"
        resultado = self.__formatear_texto(info)    # <-- Llamada interna
        print(resultado)


bot = Robot("R2D2", 1.2)
bot.mostrar_identidad()
