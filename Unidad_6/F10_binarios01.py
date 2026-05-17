""" ARCHIVOS BINARIOS

    Fuera del mundo de pickle (que guarda datos exclusivos de Python), el 
    manejo de archivos binarios directos es una de las habilidades más bajas y 
    potentes en la ingeniería. Se utiliza cuando necesitas manipular archivos 
    cuyo contenido no es texto legible, sino flujos de bytes puros, como 
    imágenes (PNG, JPEG), archivos de audio (MP3), videos o ejecutables.

    Cuando abres un archivo en modo binario nativo (usando la letra b en los 
    modos, como 'rb' o 'wb'), Python NO INTENTA TRADUCIR LOS BYTES A LETRAS o 
    caracteres UTF-8. Te da acceso directo a los números binarios (en formato 
    hexadecimal) que componen el archivo.

    Analogía: El escáner de rayos X
    -------------------------------
    **) Modo texto ('r'): Es como leer un libro. Python asume que cada byte 
        representa una letra que tú puedes pronunciar y entender.
    **) Modo binario ('rb'): Es como pasar el archivo por una máquina de 
        rayos X. No te importan las palabras; quieres ver los huesos del 
        archivo (sus bytes exactos), sin importar si es una foto de Acapulco 
        o una canción.

    Ejemplo: DUPLICAR UNA IMAGEN (CLONACIÓN DE BYTES)
    La forma más sencilla de entender esto es copiando una imagen binaria de 
    un lugar a otro. No necesitamos saber cómo se dibuja un píxel; solo 
    necesitamos leer sus bytes del archivo original y escribirlos exactamente 
    igual en un archivo nuevo.
"""
from pathlib import Path

                            # Colocar una foto en tu carpeta de usuario
                            # y renombrarla con el nombre paisaje
# ruta_original = Path.home() / "paisaje.png"
ruta_original = Path.cwd() / "paisaje.png"
ruta_copia = Path.cwd() / "copia_paisaje.png"

print('Ruta original:', ruta_original)
print('Ruta copia:', ruta_copia)

                            # Verificamos si existe la imagen original antes 
                            # de leer
if ruta_original.exists():
                            # 'rb' = Leer Binario | 'wb' = Escribir Binario
    with open(ruta_original, "rb") as archivo_origen:
                            # Leemos el flujo de bytes puro
        bytes_imagen = archivo_origen.read() 
        
    with open(ruta_copia, "wb") as archivo_destino:
                            # Volcamos los bytes exactos
        archivo_destino.write(bytes_imagen) 
        
    print("Imagen clonada byte por byte con éxito.")
else:
    print("No se encontró la imagen original para hacer la prueba.")
