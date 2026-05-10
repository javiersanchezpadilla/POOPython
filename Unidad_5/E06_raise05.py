""" RAISE

    Ejemplo completo
"""
def registrar_usuario(nombre, edad, email):
    # Validación 1: nombre no vacío
    if not nombre or len(nombre.strip()) == 0:
        raise ValueError("El nombre no puede estar vacío")
    
    # Validación 2: edad en rango
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero")
    if edad < 18:
        raise ValueError("El usuario debe ser mayor de edad")
    if edad > 100:
        raise ValueError("Edad fuera de rango (máximo 100 años)")
    
    # Validación 3: email con @
    if "@" not in email:
        raise ValueError("El email debe contener @")
    
    return f"Usuario {nombre} registrado con éxito"

# Probamos diferentes casos
try:
    registrar_usuario("", 25, "correo@mail.com")
except ValueError as e:
    print(f"Error 1: {e}")

try:
    registrar_usuario("Ana", "veinte", "ana@mail.com")
except TypeError as e:
    print(f"Error 2: {e}")

try:
    registrar_usuario("Luis", 16, "luis@mail.com")
except ValueError as e:
    print(f"Error 3: {e}")

# Caso exitoso
try:
    resultado = registrar_usuario("Carlos", 30, "carlos@mail.com")
    print(resultado)
except (ValueError, TypeError) as e:
    print(f"Error inesperado: {e}")
