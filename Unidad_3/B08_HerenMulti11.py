""" HERENCUA MULTIPLE

    La herencia múltiple es un concepto en programación orientada a objetos 
    donde una clase puede heredar atributos y métodos de más de una clase 
    padre. Esto permite que una subclase combine funcionalidades de varias 
    clases, lo que puede ser útil para modelar situaciones complejas.  

    La Herencia Múltiple es cuando una clase hija hereda atributos y métodos 
    de más de una clase padre. Es como si un objeto tuviera dos 'moldes' 
    diferentes al mismo tiempo.

    Es una herramienta muy potente, pero hay que usarla con cuidado para no 
    confundir al programa sobre qué método usar si ambos padres tienen uno con 
    el mismo nombre.

    El Reloj Inteligente (SmartWatch)
    ---------------------------------
    Imagina que tenemos una clase Reloj y una clase Telefono. Un SmartWatch es 
    ambas cosas a la vez.
"""
class Reloj:
    def mostrar_hora(self):
        print("Mostrando la hora: 09:00 AM")

class Telefono:
    def realizar_llamada(self):
        print("Conectando llamada...")

class SmartWatch(Reloj, Telefono):
    """Hereda de dos padres diferentes."""
    def mostrar_notificacion(self):
        print("Nueva notificación de WhatsApp")

# El objeto tiene las capacidades de ambos padres
mi_reloj = SmartWatch()
mi_reloj.mostrar_hora()      # Viene de Reloj
mi_reloj.realizar_llamada()  # Viene de Telefono
mi_reloj.mostrar_notificacion()
