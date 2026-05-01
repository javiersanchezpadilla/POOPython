""" PATRONES DE DISEÑO (ESTRUCTURALES)

    4. Patrones Estructurales: Ejemplo - Facade (Fachada)
    -----------------------------------------------------
    El patrón Facade proporciona una interfaz simplificada para un conjunto 
    complejo de clases (un subsistema).

    Ejemplo práctico: Encender una computadora. Tú solo presionas un botón 
    (la fachada), pero internamente el sistema debe verificar el suministro 
    eléctrico, iniciar el BIOS, cargar el kernel y montar el sistema de archivos.


"""
class CPU:
    def iniciar(self): print("CPU lista")

class Memoria:
    def cargar(self): print("Memoria cargada")

class ComputadoraFachada:
    def __init__(self):
        self.cpu = CPU()
        self.memoria = Memoria()

    def encender(self):
        print("Iniciando proceso complejo...")
        self.cpu.iniciar()
        self.memoria.cargar()
        print("Computadora lista para usar")

# El usuario solo interactúa con la fachada
pc = ComputadoraFachada()
pc.encender()
