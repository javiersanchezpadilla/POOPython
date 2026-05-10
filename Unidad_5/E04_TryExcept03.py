""" MANEJO DE EXCEPCIONES (CASOS ESPECIALES):
    USO DE EXCEPT SIN ESPECIFICAR TIPO (CAPTURA CUALQUIER EXCEPCIÓN).

    Ejemplo: Garantizar limpieza con finally + except genérico

    1)  Si el archivo no existe --> except + finally cierra (aunque archivo es
        None, NO FALLA).
    2)  Si el archivo existe pero tiene texto (hola en lugar de 123) --> 
        except captura el ValueError.
    3)  Si el archivo se abre pero disco falla (raro) --> también lo captura.

    Ventaja: El bloque finally siempre cierra el archivo, hayas tenido error o 
    no. Y el except genérico evita que el programa explote.
   
"""
def procesar_datos():
    archivo = None
    try:
        archivo = open("config.txt", "r")
        datos = archivo.read()
        numero = int(datos)  # puede fallar si no es número
        print(f"El doble es: {numero * 2}")
    except:
        print("Error inesperado. No pude procesar los datos.")
    finally:
        if archivo:
            archivo.close()
            print("Archivo cerrado (pase lo que pase).")


# Ejecutamos
procesar_datos()
