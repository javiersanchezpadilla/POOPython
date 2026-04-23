""" OVERRIDING (Extensión de funcionalidad)

    Overriding (Herencia): Es parte del diseño de clases. Es planeado y 
    estructurado. El hijo dice: 'Yo sé hacer lo mismo que mi padre, pero a mi 
    manera'.

    Concepto        ¿Dónde ocurre?      ¿Cómo funciona?     Ejemplo práctico
    --------------------------------------------------------------------------
    Overriding      En la Clase Hija    El hijo tiene su    Un Perro ladra en 
    (sobrescritura)                     propia version      vez de solo 'hacer
                                        del método del      ruido'como el 
                                        padre               animal
                                                            
    Overwriting     En el Objeto        Se reemplaza el     Un Robot que se 
    (Anulación)                         método por algo     rompe y su método 
                                        nuevo               caminar se cambia 
                                        dinámicamente       por una función de 
                                                            error.    
"""

class Profesor:

    def __init__(self, nombre_completo, id_profesor):
        self.nombre_completo = nombre_completo
        self.id_profesor = id_profesor
        

    def bienvenidos_estudiantes(self):
        print(f"Bienvenidos a clase!! Soy su profesor, mi nombre es {self.nombre_completo}")


class ProfesorDeCiencias(Profesor):

    # Está es la versión oritinal antes de la modificación
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
