""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    USO DE EXCEPT SIN ESPECIFICAR TIPO (CAPTURA CUALQUIER EXCEPCIÓN).

    Ejemplo: Capturar cualquier error al convertir números

    ¿Qué errores captura?
    ---------------------

    Si el usuario escribe:

    hola    --> ValueError  -->  entra al except.
    5.6.7   --> ValueError  -->  entra al except.
    None    --> TypeError   -->  también entra.
    5       --> es correcto, devuelve 5.0.

"""
def obtener_numero_seguro():
    entrada = input("Escribe un número: ")
    try:
        numero = int(entrada)
        return numero
                # No especificamos el tipo de error, lo manejamos solo
                # como un error generico, realmente no tengo control del 
                # error solo se que existe un error y lo atrapo
    except:
        print("No entendí lo que escribiste. Usaré el número 0.")
        return 0

# Probamos
resultado = obtener_numero_seguro()
print(f"El número es: {resultado}")
