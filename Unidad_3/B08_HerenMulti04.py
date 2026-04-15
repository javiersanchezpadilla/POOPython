""" HERENCIA MULTINIVEL CON MÉTODOS __init__ EN CADA NIVEL.

    Cada nivel de la jerarquía suele tener algo nuevo que configurar, por lo 
    que cada uno necesita su propio __init__().
    La clave para que esto funcione sin romper la cadena es el uso de 
    super().__init__().

    ¿Cómo se ejecutaría? (El flujo de ejecución)
    --------------------------------------------
    En Python, el flujo sigue una estructura de "Cebolla" o LIFO (Last In, 
    First Out):
    1)  Se entra al __init__ del Nieto.
    2)  El Nieto llama a super(), entrando al __init__ del Padre.
    3)  ElPadre llama a super(), entrando al __init__ del Abuelo.

    Se termina de ejecutar el Abuelo, luego regresa al Padre para terminarlo, 
    y finalmente regresa al Nieto.

    Análisis:
    ---------
    1)  La cadena de parámetros: Nota cómo Laptop recibe 3 datos, pero solo 
        se queda con 1 (bateria). Los otros dos los "pasa hacia arriba" a 
        través de super().
    2)  Responsabilidad Única: * El Abuelo sabe de marcas.
        *) El Padre sabe de modelos de chips.
        *) El Nieto sabe de ensamblaje final.
    3)  El orden de los print: Verán que los mensajes aparecen en orden 
        1 -> 2 -> 3. Esto confirma que la base se construye antes que la 
        especialización.

    El error común:
    ---------------
    A veces olvidamos poner los argumentos en el super(). Es vital recordar
    'Si tu padre necesita un dato para existir, tú tienes la obligación de 
    pedírselo al usuario y entregárselo a tu padre mediante super().'

    Jerarquía de una Computadora
    ----------------------------
    Vamos a ver cómo cada nivel añade una pieza de información específica.
"""
class Componente:
    def __init__(self, fabricante):
        self.fabricante = fabricante
        print(f"1. Abuelo: Fabricante '{self.fabricante}' registrado.")

class Procesador(Componente):
    def __init__(self, fabricante, modelo):
        # Llamamos al abuelo para que guarde el fabricante
        super().__init__(fabricante) 
        self.modelo = modelo
        print(f"2. Padre: Modelo '{self.modelo}' configurado.")

class Laptop(Procesador):
    def __init__(self, fabricante, modelo, bateria):
        # Llamamos al padre para que guarde fabricante y modelo
        # Tomamos el valor que requerimos y el resto lo subimos a la cadena 
        # de super()
        super().__init__(fabricante, modelo)
        self.bateria = bateria
        print(f"3. Nieto: Batería de {self.bateria} mAh instalada.")

# Instanciación
print("--- Iniciando construcción de Laptop ---")
mi_computadora = Laptop("Intel", "i7", 5000)
