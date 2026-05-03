""" MANEJO DE EXCEPCIONES.

    Jerarquía de Excepciones
    ------------------------
    Es importante entender que las excepciones son objetos y siguen una 
    jerarquía de herencia. Todas heredan de la clase BaseException.

    1)  ArithmeticError: Para errores de cálculo (como ZeroDivisionError).
    2)  LookupError: Cuando no se encuentra un índice en una lista o una 
        clave en un diccionario.
    3)  TypeError: Cuando intentas una operación con un tipo de dato 
        incorrecto.

    Lanzar tus propias excepciones (raise)
    --------------------------------------
    A veces queremos forzar un error si una regla de negocio no se cumple. 
    Para eso usamos raise.
"""
def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser un número negativo.")
    return "Edad válida"

try:
    verificar_edad(-5)
except ValueError as error:
    print(error)
