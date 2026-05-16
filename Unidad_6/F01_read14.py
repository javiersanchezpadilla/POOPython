""" MANEJO DE EXCEPCIONES

    El manejo de excepciones mediante esta forma de manipular los archivos no es 

    Explicación:
    ------------
    1)  Inicialización (archivo = None): Si el archivo no existe, la función 
        open() fallará antes de asignar nada a la variable archivo. Si no la 
        inicializamos antes, el bloque finally intentará cerrar algo que ni 
        siquiera existe en memoria, provocando un nuevo error (NameError).
    2)  La condición if archivo is not None:: Solo intentamos cerrar el 
        archivo si realmente se logró abrir con éxito.
    3)  finally: Aunque el return archivo.read() parece cortar la función, 
        Python pausa un momento el retorno (return), ejecutar obligatoriamente 
        lo que está dentro de finally (cerrar el archivo) y luego entregar el 
        contenido al print(contenido).

    Existe una mejor forma para el manejo de archivos, pero de momento debemos 
    entender como opera la forma tradicional del manejo de archivod.
"""

def leer_archivo(ruta_archivo):
    archivo = None          # <-- Inicializamos en None por si open() falla 
    try:
        archivo = open(ruta_archivo, 'r', encoding='utf8')
        return archivo.read()
    
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe.")

    except PermissionError:
        print("No tienes permisos para leer este archivo.")

    except Exception as e:
        print(f"Error inesperado: {e}")

    finally:
        # El bloque finally se ejecuta SI O SI, protegiendo el recurso
        if archivo is not None:
            archivo.close()
            print("Archivo cerrado correctamente desde el bloque 'finally'.")


contenido = leer_archivo("/home/javier/Documentos/Programas/Python/POOPython/datos.txt")
print(contenido)
