""" DECORADOR @contextmanager

    El decorador @contextmanager es una alternativa más rápida y directa para 
    crear gestores de contexto sin tener que escribir una clase completa con 
    los métodos __enter__() y __exit__().
    Para usarlo, combinamos dos conceptos avanzados: Los decoradores y los 
    generadores (funciones que usan la palabra clave yield en lugar de return)

    Analogía: El Sándwich de Código
    ---------------------------------
    Imagina que @contextmanager te permite dividir una función en tres partes 
    bien definidas, como si fuera un sándwich:

    1)  La tapa superior (Antes del yield): Todo el código que se ejecuta al 
        entrar al bloque with. Aquí pides recursos, inicias cronómetros o 
        abres conexiones.
    2)  El relleno (El yield): Es la pausa. El programa se detiene aquí, le 
        entrega el control al bloque with para que ejecute sus tareas internas 
        y, opcionalmente, le manda un objeto a la variable del 'as'.
    3)  La tapa inferior (Después del yield): Todo el código que se ejecuta al 
        salir del bloque with. Aquí limpias memoria, cierras recursos o apagas 
        interruptores.

    Ejemplo: El Cronómetro (nueva versión y simplificada).
    ------------------------------------------------------
    Vamos a reescribir el ejemplo del cronómetro, pero ahora usando el 
    decorador. (Notarás que el código se reduce drásticamente)
"""
import time
from contextlib import contextmanager

@contextmanager
def cronometro_corto():
    # 1. CÓDIGO DE ENTRADA (__enter__)
    inicio = time.time()
    print("[Inicio] Midiendo tiempo...")
    
    try:
        # 2. LA PAUSA: Aquí el programa ejecuta el cuerpo del 'with'
        yield 
    finally:
        # 3. CÓDIGO DE SALIDA (__exit__)
        # El finally garantiza que se mida el tiempo aunque falle el código de adentro
        fin = time.time()
        print(f"[Fin] Tiempo total: {fin - inicio:.4f} segundos.")


# Uso del decorador
with cronometro_corto():
    print("   Ejecutando proceso A...")
    time.sleep(0.8)
