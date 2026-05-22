""" USO DE WITH, ARCHIVOS Y CONTEXT MANAGER EN PYTHON

    Ejemplo: El Interruptor de Modo Pruebas (Modificar un Estado Global)
    Imagina que tienes un sistema y quieres activar temporalmente un Modo 
    Depuración o Modo Dios, solo para unas líneas de código específicas, pero 
    necesitas garantizar que al salir el sistema vuelva a la normalidad de 
    manera segura.

    Los Parámetros del Método __exit__()
    ------------------------------------
    __exit__() siempre recibe tres argumentos adicionales: tipo, valor y traza 
    (en inglés comúnmente nombrados exc_type, exc_val, exc_tb).
    Si el bloque de código dentro del with se ejecuta perfectamente, estos 
    tres parámetros valdrán None.
    Si ocurre un error dentro del with, Python no detiene el programa de 
    inmediato; primero va a __exit__() y te envía los detalles del error en 
    esas tres variables para que decidas qué hacer.
    Esta estructura garantiza que, incluso si el código del falla(se rompe o
    truena) a mitad de un proceso, la sección __exit__() se ejecutará de forma 
    prioritaria para limpiar la memoria o restaurar los valores del sistema.
"""
class ModoSimulacion:
    # Atributo de clase global ficticio
    sistema_en_pruebas = False

    def __enter__(self):
        # Activamos el estado especial al entrar
        ModoSimulacion.sistema_en_pruebas = True
        print("[SISTEMA] Modo Simulación: ACTIVADO.")
        return self

    def __exit__(self, tipo, valor, traza):
        # Restauramos el estado original pase lo que pase al salir
        ModoSimulacion.sistema_en_pruebas = False
        print("[SISTEMA] Modo Simulación: DESACTIVADO. Volviendo a producción.")

# Uso del Interruptor
print(f"¿El sistema está en pruebas?: {ModoSimulacion.sistema_en_pruebas}")

with ModoSimulacion():
    print("-> Ejecutando pruebas críticas de inyección de código...")
    print(f"-> ¿El sistema está en pruebas?: {ModoSimulacion.sistema_en_pruebas}")

print(f"¿El sistema está en pruebas?: {ModoSimulacion.sistema_en_pruebas}")
