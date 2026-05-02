""" PATRONES DE DISEÑO CREACIONALES

    El Gestor de Logs (Historial del Sistema)
    -----------------------------------------
    Imagina que tienes una aplicación con muchas partes (un módulo de red, uno 
    de interfaz y uno de base de datos). Quieres que todos escriban en el 
    mismo archivo de texto y no que cada uno cree un archivo diferente.

    
"""
class LoggerSistema:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(LoggerSistema, cls).__new__(cls)
            # Simulamos la apertura de un único archivo
            cls._instancia.archivo = "log_general.txt"
        return cls._instancia

    def registrar_evento(self, mensaje):
        print(f"Escribiendo en {self.archivo}: {mensaje}")

# Uso en diferentes partes del código
log_red = LoggerSistema()
log_db = LoggerSistema()

log_red.registrar_evento("Error de conexión al servidor")
log_db.registrar_evento("Usuario 'Javier' inició sesión")

print(f"¿Ambos usan el mismo archivo? {log_red is log_db}")
