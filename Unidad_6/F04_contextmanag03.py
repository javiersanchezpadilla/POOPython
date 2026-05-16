""" USO DE WITH, ARCHIVOS Y CONTEXT MANAGER EN PYTHON

    Manejo de Excepciones
    ---------------------
    ¿Qué pasa si ocurre un error dentro de nuestro código? para evitar que
    nuestro código se rompa usamos with combinado con try - except, actuando 
    como un bloque try-finally automático.
    En este ejemplo vamos a simular un error de división entre cero 
    inmediatamente después de abrir el archivo y la pregunta ahora es 

    Pregunta: ¿El archivo se quedó abierto debido al error de división?
    Respuesta: NO. 'with' garantizó el cierre del archivo antes de que el 
    error pasara al 'except'.

"""
try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
        # Simulamos un error grave de cálculo con los datos
        resultado = 10 / 0 

except ZeroDivisionError:
    print("Ocurrió una división entre cero.")

