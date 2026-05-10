""" RAISE

    raise ZeroDivisionError("No se puede dividir")

    ¿Cuándo usarlo?
    ---------------
    *)  Cuando quieres reemplazar el mensaje genérico por uno más claro
    *)  Cuando adaptas un error existente a tu contexto específico
    *)  Cuando la excepción original tiene un mensaje confuso
"""
def division_segura(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

# Probamos
try:
    division_segura(10, 0)
except ZeroDivisionError as e:
    print(f"Error personalizado: {e}")
