""" ARCHIVOS BINARIOS

    Ejemplo Modificar un Byte específico (Inyección o Edición)
    ----------------------------------------------------------
    Trabajar en binario permite hacer cambios dentro de los archivos. 
    Imagina que tienes un archivo binario de datos y necesitas cambiar un 
    único valor sin alterar el resto del archivo.

"""
                            # Creamos un flujo de bytes simulado (como una 
                            # cadena de bytes con la letra 'b')
                            # Cada letra representa un byte en memoria
datos_sensores = bytearray(b"TEMP:25C") 
print(datos_sensores)

print(f"Datos originales: {datos_sensores.decode('utf-8')}")

                            # Modificamos directamente el byte en la posición 
                            # 5 (donde está el número 2)
                            # El número 51 en código ASCII representa al 
                            # carácter '3'
datos_sensores[5] = 51 

print(f"Datos modificados en binario: {datos_sensores.decode('utf-8')}")
