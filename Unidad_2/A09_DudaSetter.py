""" Aclaración sobre la implementación de setter

    En el código presentado existe un atributo protegido (self.__escudo), 
    la clase ya contiene su getter y su setter y se creó una propiedad 
    (escudo), sin embargo ¿es correcto que desde el método sufrir_danio(self) 
    se acceda a la propiedad (escudo), en lugar de modificar el atributo de 
    instancia protegido (self.__escudo)?

    Este planteamiento toca un punto fundamental de la arquitectura limpia 
    en programación.

    La respuesta es: Sí, es correcto y, de hecho, es la mejor práctica.
    Se debe preferir usar self.escudo (la propiedad) en lugar de self.__escudo 
    (el atributo privado) dentro de la misma clase:

    1. Centralización de la Lógica (El "Portero")
    ---------------------------------------------
    Imagina que el Setter es un portero que revisa quién entra. Si en el futuro 
    decides que el escudo nunca puede ser menor a 0, añadirás esa lógica dentro 
    del @escudo.setter.

    Si usas self.escudo -= 5: El "portero" (Setter) revisará la operación y 
    detendrá el valor si intenta bajar de cero.

    Si usas self.__escudo -= 5: Estás saltándote al portero. Podrías terminar 
    con un escudo de -5, -10, etc., rompiendo las reglas de tu propia clase.

    2. Mantenimiento y Evolución del Código
    ---------------------------------------
    Si el día de mañana cambias la forma en que se calcula el daño (por ejemplo, 
    que el escudo se reduzca de forma distinta si el valor es muy bajo), solo 
    tendrías que cambiar el código en un solo lugar (el Setter).

    Si usaras el atributo privado en todos tus métodos (sufrir_danio, 
    recargar, reparar), tendrías que buscar y modificar cada uno de esos métodos 
    cuando las reglas cambien.
"""
class Nave:

    def __init__(self, escudo):
        self.__escudo = escudo

    @property 
    def escudo(self):
        return self.__escudo 
    
    @escudo.setter 
    def escudo(self, new_escudo):
        self.__escudo = new_escudo

    def sufrir_danio(self):
        # self.__escudo -= 5    # Esta es la manera en que no se recomienda usar
                                # porque puede romper nuestras propias reglas de 
                                # la clase, al usar el setter administramos las 
                                # reglas que establecimos como limites o condiciones
        self.escudo -= 5        # Aqui usamos el setter en lugar de self.__escudo

n1 = Nave(100)
n1.sufrir_danio()
n1.sufrir_danio()
print(n1.escudo)


