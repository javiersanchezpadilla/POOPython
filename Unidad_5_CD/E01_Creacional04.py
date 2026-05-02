""" DISEÑO DE PATRONES

    Control de Sensor de Huella (Acceso Único)
    En ingeniería de hardware, a veces un componente físico no puede ser 
    controlado por dos objetos al mismo tiempo porque causaría un conflicto 
    eléctrico o de memoria. El Singleton asegura que solo exista un 'director'
    para ese sensor.

    Resumen Final de Patrones Creacionales
    --------------------------------------
    Con el Singleton y el Factory Method que vimos antes, entendemos:

    1)  No siempre es bueno dejar que cualquiera cree objetos a lo loco.
    2)  A veces es mejor tener un 'Gerente de Creación' (Factory).
    3)  A veces es obligatorio que solo exista un ejemplar (Singleton).
"""
class LectorHuella:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("--- Inicializando hardware del sensor de huella ---")
            cls._instancia = super(LectorHuella, cls).__new__(cls)
        return cls._instancia

    def escanear(self):
        print("Escaneando huella dactilar... ¡Acceso concedido!")

# Dos programas intentan usar el sensor
admin_acceso = LectorHuella()
seguridad_puerta = LectorHuella()

admin_acceso.escanear()
# No se vuelve a inicializar el hardware, se usa el mismo objeto
seguridad_puerta.escanear()
