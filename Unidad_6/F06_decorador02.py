""" DECORADOR @contextmanager

    ¿Cómo funciona el as con yield?
    -------------------------------
    En la versión con clases, usábamos return self para mandar el objeto a la 
    variable después del 'as'. Con @contextmanager, lo que sea que pongas al 
    lado derecho de la palabra 'yield' es lo que recibirá la variable del 'as'

    Imaginemos un gestor que simula la apertura segura de una libreta de 
    calificaciones para un alumno:
"""
from contextlib import contextmanager

@contextmanager
def abrir_boleta(nombre_alumno):
    print(f"Abriendo expediente de: {nombre_alumno}")
    # Creamos un diccionario simulación
    boleta = {"Alumno": nombre_alumno, "POO": 95, "Estructura_Datos": 90}
    
    try:
        # Enviamos la boleta al bloque 'with' usando yield
        yield boleta 
    finally:
        # Al terminar, guardamos cambios de forma segura
        print("Guardando cambios y cerrando expediente en la base de datos.")

# Uso con la palabra 'as'
with abrir_boleta("Carlos Flores") as expediente:
    # 'expediente' toma el valor del diccionario que enviamos en el yield
    print(f"   Modificando calificación actual de POO: {expediente['POO']}")
    expediente["POO"] = 100
