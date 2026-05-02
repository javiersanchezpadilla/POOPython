""" PATRONES DE DISEÑO ESTRUCTURALES (ADAPTER)

    Es el más famoso de los estructurales y es perfecto para ingenieros porque 
    funciona igual que un adaptador de corriente real: permite que dos clases 
    con interfaces incompatibles trabajen juntas.

    El Patrón Adapter es uno de los más agradecidos de enseñar en Ingeniería 
    porque tiene una utilidad práctica inmediata: conectar código viejo 
    (Legacy) con código nuevo sin romper nada.

    Patrón Estructural: Adapter (Adaptador)
    ---------------------------------------
    *)  El Problema: Tienes una clase antigua que funciona perfectamente, pero 
        sus métodos no coinciden con la nueva interfaz que estás diseñando. No 
        puedes (o no quieres) modificar la clase vieja porque podrías romper 
        otras partes del sistema.
    *)  La Solución: Creas una clase intermedia (el Adaptador) que 'envuelve' 
        a la clase vieja y traduce las llamadas de la interfaz nueva a la 
        antigua.

    Ejemplo: El sistema de cobro de la Facultad
    -------------------------------------------
    Imagina que estás modernizando el sistema de pagos. El sistema nuevo espera 
    que todos los métodos se llamen procesar_pago(cantidad), pero tienes una 
    clase vieja de un banco externo que usa el método 
    realizar_transaccion_bancaria(monto_mxn).

    ¿Por qué es un patrón Estructural?
    ----------------------------------
    Porque no nos preocupa cómo se crea el objeto (creacional), ni cómo se 
    comunican (comportamiento), sino cómo se ensamblan las piezas para que la 
    estructura del software sea coherente.
"""
# 1. La Clase Vieja (Legacy) - No la podemos tocar
class BancoAntiguo:
    def realizar_transaccion_bancaria(self, monto_mxn):
        print(f"Procesando ${monto_mxn} MXN a través del protocolo antiguo del banco...")

# 2. La Interfaz Nueva (Lo que esperamos ahora)
from abc import ABC, abstractmethod

class SistemaPagoNuevo(ABC):
    @abstractmethod
    def procesar_pago(self, cantidad):
        pass

# 3. EL ADAPTADOR: El puente entre lo viejo y lo nuevo
class AdaptadorBanco(SistemaPagoNuevo):
    def __init__(self, objeto_banco_antiguo):
        self.banco_antiguo = objeto_banco_antiguo

    def procesar_pago(self, cantidad):
        # Aquí ocurre la traducción:
        # El sistema nuevo llama a 'procesar_pago', 
        # y el adaptador lo traduce a 'realizar_transaccion_bancaria'
        self.banco_antiguo.realizar_transaccion_bancaria(cantidad)

# --- USO EN EL SISTEMA ---

banco_viejo = BancoAntiguo()
# El sistema nuevo no sabe usar 'banco_viejo' directamente...
# Así que usamos el adaptador:
pago_moderno = AdaptadorBanco(banco_viejo)

# Ahora el sistema nuevo puede usarlo sin problemas
pago_moderno.procesar_pago(1500)
