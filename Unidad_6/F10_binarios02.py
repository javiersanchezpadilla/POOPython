""" ARCHIVOS BINARIOS

    ¿Cuándo usar manejo binario directo en lugar de JSON/Pickle?
    ------------------------------------------------------------
    1)  Transferencia de archivos (Sockets/Red): Cuando programas un servidor 
        que va a recibir o enviar imágenes o archivos adjuntos que los 
        usuarios suben.
    2)  Procesamiento de Multimedia: Extraer los metadatos de una canción 
        (título, artista) leyendo los bytes del final de un archivo MP3 
        (etiquetas ID3)
    3)  Criptografía y Compresión: Al diseñar algoritmos que necesitan aplicar 
        compuertas lógicas (AND, XOR) bit a bit a un archivo para encriptarlo.


    Ejemplo: Leer la Firma o Cabecera de un archivo (Metadata)
    ----------------------------------------------------------
    Todos los archivos binarios estándar tienen los primeros bytes reservados 
    para identificarse ante el sistema operativo. A estos bytes iniciales se 
    les conoce como 'Magic Numbers' (Números Mágicos) o firmas de archivo.

    Por ejemplo, un documento PDF legítimo siempre, por estándar internacional
    empieza con los mismos 4 bytes en código ASCII.%PDF (ver resultado de 
    ejecución del programa)

    Vamos a hacer un programa muy simple que lea los primeros 4 bytes de un 
    archivo para verificar si realmente es un PDF legítimo o si alguien solo 
    le cambió la extensión a un archivo falso:
"""
from pathlib import Path

ruta_documento = Path.cwd() / "documento_catedra.pdf"

                            # Simulamos la creación de un PDF de prueba rápido 
                            # solo para el ejemplo
ruta_documento.write_bytes(b"%PDF-1.4\n1 0 obj ...") 

                            # Abrimos en modo binario
with open(ruta_documento, "rb") as f:
                            # Leemos ÚNICAMENTE los primeros 4 bytes del 
                            # archivo
    primeros_bytes = f.read(4) 
    
    print(f"Bytes crudos recuperados: {primeros_bytes}")
    
                            # Comparamos la firma binaria estándar de los 
                            # archivos PDF
    if primeros_bytes == b"%PDF":
        print("Verificación exitosa: Estructura de cabecera válida para un PDF.")
    else:
        print("Alerta de Seguridad: El archivo no tiene la firma digital de un PDF.")
