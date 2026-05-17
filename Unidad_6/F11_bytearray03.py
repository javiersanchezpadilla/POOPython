""" BYTEARRAY

    ¿Por qué es útil en la Ingeniería de Software?
    -----------------------------------------------
    Un bytearray no se usa para escribir texto común (para eso ya están los 
    strings). Se utiliza en escenarios de alto rendimiento y bajo nivel:

    1)  Búfer de Red (Sockets): Cuando una computadora está recibiendo una 
        imagen pesada o un archivo desde internet, los datos llegan por 
        pedazos de bytes. El programa los va acumulando dentro de un bytearray 
        (usando .append()) hasta que el archivo se completa.
    2)  Criptografía básica: Si quieres encriptar un mensaje de forma rápida, 
        puedes tomar un bytearray, recorrerlo con un ciclo y sumarle un número 
        a cada byte (un cifrado César). Al cambiar los números, el texto se 
        vuelve ilegible hasta que hagas el proceso inverso.
    3)  Ahorro de memoria RAM: Modificar un string gigante en Python obliga a
        la computadora a duplicar el espacio en la memoria RAM para crear el 
        nuevo string. Modificar un bytearray altera los datos directamente en 
        la celda de memoria original sin gastar espacio extra.


    Ejemplo: Modificar un byte directo
    -----------------------------------
    Como es una colección indexada, podemos acceder a cualquier posición 
    usando corchetes [] y cambiar su valor numérico directamente.
    Queremos cambiar la palabra 'HOLA' por 'HOLO'.
    Sabemos que la letra 'A' está en la posición [3]. Queremos cambiarla 
    por una 'O', y el código ASCII para la 'O' mayúscula es el número 79.
"""
letrero = bytearray("HOLA", "utf-8")

                            # Modificamos directamente el byte en el índice 3
letrero[3] = 79 

print(f"Resultado en bytes: {letrero}")

                            # Para volver a ver el texto normal y legible, 
                            # usamos .decode()
texto_final = letrero.decode("utf-8")
print(f"Texto decodificado: {texto_final}")
