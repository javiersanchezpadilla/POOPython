""" BYTEARRAY

    Para entender bytearray, primero debemos recordar que la computadora no 
    entiende letras, ni palabras, ni imágenes; solo entiende números 
    (específicamente bytes). Un byte es un conjunto de 8 bits y puede 
    representar cualquier número entero entre el 0 y el 255.

    En Python, un bytearray es simplemente una lista o arreglo de números 
    (bytes) que se puede modificar.

    Analogía
    --------
    El letrero de hotel con focos cambiables
    Imagina que tienes un letrero luminoso en la entrada de un hotel que dice 
    'HOLA', Cada letra está formada por un foco de color específico.

    **) Un string normal (HOLA): Es como si el letrero estuviera fundido en 
        una sola pieza de plástico. Si quieres cambiar la 'A' por una 'O' para 
        que diga 'HOLO', no puedes modificar el letrero directamente. Tienes 
        que tirar el letrero viejo a la basura y fabricar uno completamente 
        nuevo desde cero. En programación, a esto se le llama ser INMUTABLE.
    **) Un bytearray: Es un letrero donde cada foco se puede desatornillar 
        individualmente. Si quieres cambiar la 'A' por la 'O', vas a la última 
        posición, quitas el foco de la 'A', pones el de la 'O' y listo. El 
        letrero sigue siendo el mismo, pero cambiaste una parte interna. 
        A esto se le llama ser MUTABLE (modificable).

    ¿Cómo se crea un bytearray?
    ---------------------------
    Podemos crear un bytearray de varias formas, pero las dos más comunes son: 
    definiendo un tamaño vacío o convirtiendo un texto existente (indicando su 
    codificación, que normalmente es utf-8).
"""
                            # Método A: Crear un bytearray vacío con espacio 
                            # para 5 bytes (inicializados en 0)
memoria_vacia = bytearray(5)
print(f"Espacio reservado: {memoria_vacia}") 
                            # Salida en consola: 
                            # bytearray(b'\x00\x00\x00\x00\x00') 
                            #             \x00 = cero en hexadecimal

                            # Método B: Convertir un texto a bytes modificables
letrero = bytearray("HOLA", "utf-8")
                            # Salida en consola: bytearray(b'HOLA')
print(f"Letrero original: {letrero}")
