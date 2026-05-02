""" PATRÓN FACTORY (CREACIONAL)

    El objetivo es crear objetos sin que el usuario sepa la clase exacta, solo 
    pide un tipo.

    1. Fábrica de Notificaciones (Mensajería)
    ------------------------------------------
    Dependiendo de la preferencia del usuario, el sistema envía un mensaje por 
    diferentes canales.
"""
class Email:
    def enviar(self): return "Enviando correo electrónico..."

class SMS:
    def enviar(self): return "Enviando mensaje de texto..."

class FabricaComunicaciones:
    @staticmethod
    def crear_canal(tipo):
        if tipo == "email": return Email()
        if tipo == "sms": return SMS()

# Uso: El sistema no sabe qué es, solo que envía.
canal = FabricaComunicaciones.crear_canal("email")
print(canal.enviar())
