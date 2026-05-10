""" RAISE

    raise (relanzar la última excepción)

    Sintaxis: 
            raise (solito, sin nada más)

            
    Resultado esperado:
    --------------------
    *)  El archivo no existe --> ocurre FileNotFoundError
    *)  El except lo captura, registra un mensaje
    *)  raise (solito) relanza el mismo error
    *)  El error sube al bloque try exterior
    *)  El programa principal también lo captura


    ¿Cuando usarlo?
    ---------------

    *)  Cuando quieres registrar (log) un error pero también dejarlo que suba
    *)  Cuando haces una limpieza parcial y luego quieres que el error siga su 
        curso
    *)  Cuando no puedes resolver el error ahí, pero quieres dejar evidencia
"""
def procesar_archivo(nombre):
    try:
        archivo = open(nombre, "r")
        contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print("Registrando en log: archivo no encontrado")
        raise  # Relanza el mismo error que acaba de ocurrir

# Probamos
try:
    procesar_archivo("no_existe.txt")
except FileNotFoundError:
    print("El programa principal también capturó el error")
