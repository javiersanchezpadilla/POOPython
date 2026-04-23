""" OVERWRITTING (Anulación o reemplazo)

    ejemplo de Overwriting (Anulación) aplicado a una situación real de 
    ingeniería: cuando un objeto 'pierde' o 'cambia' una funcionalidad 
    debido a un estado del sistema (como un error o un cambio de modo).

    El dron fuera de control (Overwriting)
    --------------------------------------
    Imagina que tienes un dron con un método para volar. Si el dron detecta 
    una falla crítica, queremos que el método volar deje de funcionar y sea 
    reemplazado por un protocolo de 'Aterrizaje Forzoso'.

    Concepto        ¿Dónde ocurre?      ¿Cómo funciona?     Ejemplo práctico
    --------------------------------------------------------------------------
    Overriding      En la Clase Hija    El hijo tiene su    Un Perro ladra en 
    (sobrescritura)                     propia version      vez de solo 'hacer
                                        del método del      ruido'como el 
                                        padre               animal
                                                            
    Overwriting     En el Objeto        Se reemplaza el     Un Robot que se 
    (Anulación)                         método por algo     rompe y su método 
                                        nuevo               caminar se cambia 
                                        dinámicamente       por una función de 
                                                            error.
"""
class Dron:
    def volar(self):
        print("El dron está volando de forma estable.")

def protocolo_emergencia():
    print("¡ERROR CRÍTICO! El motor no responde. Aterrizando de emergencia...")

# 1. El dron opera normal
mi_dron = Dron()
mi_dron.volar()  # Salida: El dron está volando de forma estable.

# 2. Ocurre una falla (Overwriting en tiempo de ejecución)
# Aquí anulamos el método original escribiendo una nueva función sobre él
mi_dron.volar = protocolo_emergencia

# 3. Intentamos usar el mismo método
print("\n--- Intento de vuelo tras falla ---")
mi_dron.volar()
