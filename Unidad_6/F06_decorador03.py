""" DECORADOR @contextmanager

    Nivel Avanzado: Control total de errores
    ----------------------------------------
    Una de las grandes ventajas de usar @contextmanager es que el manejo de
    las excepciones internas del with se vuelve muy natural, porque se 
    controlan con un bloque try-except común y corriente dentro de la misma 
    función.

    Imagina que queremos un gestor que ignore ciertos errores menores de 
    conversión para que el programa no se rompa (no truene).

    ¿Clases o Decoradores?
    ----------------------
    **) Usa Clases (__enter__() / __exit__() ) cuando: El gestor de contexto 
        necesite mantener un estado complejo, requiera muchos atributos 
        internos o forme parte de una arquitectura de herencia de software.
    **) Usa el decorador (@contextmanager) cuando: Necesites algo rápido, 
        limpio y cuya única función sea envolver un proceso simple de 
        abrir/cerrar, conectar/desconectar o configurar/restaurar.
"""
from contextlib import contextmanager

@contextmanager
def ignorar_errores_conversion():
    print("Modo tolerante a fallos activado.")
    try:
        yield
    except ValueError as e:
        print(f"Se detectó un ValueError interno pero lo mitigamos: {e}")
    finally:
        print("Saliendo del modo tolerante a fallos.")

# Prueba del sistema
with ignorar_errores_conversion():
    print("Intentando convertir un texto a entero...")
    # Esto normalmente detendría el programa completo
    numero = int("no_soy_un_numero") 

print("El script continuó vivo gracias al gestor de contexto.")
