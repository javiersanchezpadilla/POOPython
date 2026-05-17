""" ARCHIVOS BINARIOS

    Almacenar texto en binario.
    ---------------------------

    es un excelente ejercicio para conectar la interacción con el usuario 
    (entrada por teclado) con el procesamiento de datos a bajo nivel (bytes y 
    archivos binarios).

    Para lograrlo, el flujo del programa sigue una arquitectura muy clara:

    1)  Captura: Se leen las líneas de texto desde el teclado usando input().
    2)  Conversión: Ese texto (que está en formato string) se convierte a 
        bytes (un flujo binario) mediante un proceso llamado codificación 
        (.encode()).
    3)  Persistencia: Esos bytes se escriben directamente en el disco duro 
        dentro de un archivo abierto en modo escritura binaria ('wb').
    4)  Recuperación: Se lee el archivo en modo lectura binaria ('rb'), o
        bteniendo los bytes crudos.
    5)  Decodificación: Los bytes se transforman de vuelta a texto legible 
        usando .decode() para mostrarlos en la consola.

    ¿Qué pasa en el disco duro? 
    ---------------------------
    Si intentamos abrir el archivo generado lineas_teclado.bin con un editor 
    de texto plano o desde la terminal de Linux con un comando como cat lineas_teclado.bin, es probable que alcances a leer el texto de forma normal.

¿Por qué pasa esto si es un archivo binario? Because la codificación utf-8 para caracteres occidentales (letras estándar del alfabeto) utiliza exactamente los mismos números binarios que el viejo código ASCII. Por lo tanto, los visualizadores de texto detectan esos bytes y los traducen automáticamente en pantalla.

Sin embargo, para Python, la gran diferencia radica en el flujo de control:

Al usar 'wb', le prohibimos a Python agregar caracteres ocultos de control de formato de texto (como marcas de fin de archivo o conversiones automáticas de saltos de línea de Windows a Linux \r\n).

El programa escribe y lee fielmente bit a bit lo que el usuario digitó, garantizando la integridad absoluta de los datos.
"""
from pathlib import Path

                            # Definimos la ruta del archivo binario usando 
                            # pathlib
ruta_archivo = Path.cwd() / "lineas_teclado.bin"

                            # ================================================
                            # PASO 1: Capturar 3 líneas de texto desde teclado
                            # ================================================
print("Por favor, ingresa 3 líneas de texto para guardarlas en binario:")
linea1 = input("Línea 1: ")
linea2 = input("Línea 2: ")
linea3 = input("Línea 3: ")

                            # Unimos las tres líneas en un solo bloque de 
                            # texto usando saltos de línea (\n)
texto_completo = f"{linea1}\n{linea2}\n{linea3}"


                            # ================================================
                            # PASO 2: Convertir a bytes y guardar en el 
                            # archivo binario
                            # ================================================
                            # .encode('utf-8') transforma el string en un 
                            # objeto de bytes crudos
bytes_a_guardar = texto_completo.encode('utf-8')

                            # Abrimos en modo 'wb' (Write Binary - Escritura 
                            # Binaria)
with open(ruta_archivo, "wb") as archivo_binario:
    archivo_binario.write(bytes_a_guardar)

print(f"\nEl texto ha sido convertido a bytes y guardado en: {ruta_archivo.name}")


                            # ================================================
                            # PASO 3: Recuperar el archivo binario y restaurar 
                            # el texto original
                            # ================================================
print("\nLeyendo el archivo binario desde el disco...")

                            # Abrimos en modo 'rb' (Read Binary - Lectura Bin)
with open(ruta_archivo, "rb") as archivo_binario:
    bytes_recuperados = archivo_binario.read()

                            # En este punto, 'bytes_recuperados' contiene 
                            # números hexadecimales.
                            # .decode('utf-8') hace el trabajo inverso, traduce 
                            # los bytes a texto legible.
texto_restaurado = bytes_recuperados.decode('utf-8')


                            # ================================================
                            # PASO 4: Visualizar el resultado normalmente
                            # ================================================
print("\nTexto recuperado con éxito:")
print("-" * 30)
print(texto_restaurado)
print("-" * 30)
