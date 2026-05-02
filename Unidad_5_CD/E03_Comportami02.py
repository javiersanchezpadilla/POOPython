""" PATRONES DE DISEÑO (DE COMPORTAMIENTO)

    El patrón Command es fascinante porque transforma una petición o acción en 
    un objeto independiente. En lugar de ejecutar una orden directamente, la 
    empaquetamos.

    Patrón de Comportamiento: Command (Orden)
    -----------------------------------------
    **) El Problema: Tienes un sistema donde muchas cosas pueden activar la 
        misma acción (un botón, un atajo de teclado, un comando de voz). 
        Además, quieres que tu sistema sea capaz de deshacer acciones o 
        guardarlas en una cola para ejecutarlas después.
    **) La Solución: Crear un objeto 'Comando' que contenga toda la 
        información necesaria para ejecutar la acción. Así, el objeto que 
        pide la acción no necesita saber cómo se hace, solo sabe que tiene un 
        comando que puede ejecutar.

    Ejemplo: El Sistema de Domótica (Casa Inteligente)
    --------------------------------------------------
    Imagina un control remoto universal. No queremos que el control sepa cómo 
    funciona cada foco o cada aire acondicionado; solo queremos que el control 
    dispare comandos.

    ¿Por qué es útil?
    ------------------
    1)  Sistemas de Deshacer (Undo/Redo): Al guardar los objetos comando en una 
        lista (pila), implementar el 'Deshacer' es tan simple como llamar al 
        método deshacer() del último objeto guardado.
    2)  Registro de Acciones (Transacciones): Puedes guardar todos los comandos
        ejecutados en un archivo para repetirlos si el sistema se cae.
    3)  Desacoplamiento: El botón no sabe que está encendiendo una luz; solo 
        sabe que tiene un objeto que sabe ejecutar().
"""
from abc import ABC, abstractmethod

# 1. La Interfaz Command
class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def deshacer(self):
        pass

# 2. El Receptor (Quien realmente sabe hacer el trabajo)
class Luz:
    def encender(self): print("Luz encendida")
    def apagar(self): print("Luz apagada")

# 3. Comandos Concretos
class ComandoEncenderLuz(Comando):
    def __init__(self, luz: Luz):
        self.luz = luz

    def ejecutar(self):
        self.luz.encender()

    def deshacer(self):
        self.luz.apagar()

# 4. El Invocador (El Control Remoto)
class ControlRemoto:
    def __init__(self):
        self._historial = []

    def presionar_boton(self, comando: Comando):
        comando.ejecutar()
        self._historial.append(comando)

    def presionar_deshacer(self):
        if self._historial:
            comando = self._historial.pop()
            print("Deshaciendo última acción...")
            comando.deshacer()

# --- PRUEBA ---
foco_sala = Luz()
control = ControlRemoto()

# Creamos la orden
orden_encender = ComandoEncenderLuz(foco_sala)

# El control remoto ejecuta la orden sin saber qué hace la luz por dentro
control.presionar_boton(orden_encender)
control.presionar_deshacer()
