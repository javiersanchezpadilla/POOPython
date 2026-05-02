""" PATRÓN OBSERVER (COMPORTAMIENTO)

    Modo Oscuro en una App (UI)
    ---------------------------
    Cuando el usuario cambia el tema de la aplicación, todas las ventanas 
    abiertas deben cambiar su color.

    Resumen:
    --------
    **) Factory: Es como un Vendedor de mostrador: tú le pides algo y él te lo
        entrega, tú no entras al almacén a buscarlo.
    **) Observer: Es como un Grupo de WhatsApp: alguien envía un mensaje 
        (noticia) y todos los que están en el grupo reciben la notificación y 
        deciden qué hacer.
"""
class ConfiguracionTema:
    def __init__(self):
        self.ventanas = []

    def set_tema(self, tema):
        print(f"\nCambiando tema a: {tema}")
        for v in self.ventanas:
            v.aplicar_tema(tema)

class VentanaChat:
    def aplicar_tema(self, tema): print(f"Chat: Cambiando fondo a {tema}")

class VentanaContactos:
    def aplicar_tema(self, tema): print(f"Contactos: Cambiando iconos a {tema}")

# Uso
config = ConfiguracionTema()
config.ventanas = [VentanaChat(), VentanaContactos()]
config.set_tema("Modo Oscuro")
