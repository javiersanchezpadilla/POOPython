""" El valor de retorno por defecto
    -------------------------------
    Si olvidas poner la palabra return en una función o método, Python no devuelve 
    "nada"; devuelve None automáticamente."""

def saludar():
    print("Hola")

resultado = saludar()
print(resultado)  # Imprimirá: None
