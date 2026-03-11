""" El método "Orquestador" (Nivel Proceso)

    Aquí, el método encender_auto actúa como un director de orquesta.
    No hace el trabajo solo, sino que llama a varios métodos pequeños 
    para completar una tarea compleja."""

class Automovil:
    def revisar_aceite(self):
        print("Aceite en niveles óptimos.")

    def inyectar_combustible(self):
        print("Combustible inyectado.")

    def encender_motor(self):
        # El método principal llama a los pasos previos
        self.revisar_aceite()               # <-- Llamada 1
        self.inyectar_combustible()         # <-- Llamada 2
        print("¡Motor encendido!")


mi_carro = Automovil()
mi_carro.encender_motor()
