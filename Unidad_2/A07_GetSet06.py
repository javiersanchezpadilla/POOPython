""" En este código, verás cómo protegemos la batería para que nadie pueda
    ponerle un valor negativo o mayor a 100.
    
    hemos visto que los atributos protegidos (_) y privados (__) son como 
    "cajas cerradas". Para interactuar con ellas de forma segura y profesional 
    sin romper el encapsulamiento, usamos los métodos Getters (para obtener el 
    valor) y Setters (para modificarlo).

    Este ejemplo de un Dron de Entrega, Es ideal porque algunos datos deben ser 
    públicos (como su nombre), pero otros son críticos (como el nivel de batería 
    o las coordenadas) y no pueden cambiarse a la ligera.

    Lo que hace que este no es solo esconder el atributo, sino la lógica de 
    control dentro del Setter:

    1)  Validación de Datos: En el Setter de la batería, pusimos un if. Esto evita 
        que el objeto entre en un "estado imposible" (como tener 150% de batería o -20%).
    2)  Abstracción de Lectura: El Getter no solo devuelve el número, le da formato 
        ("Nivel de batería: ...%"). Esto permite que, si el día de mañana decides cambiar 
        cómo se muestra la batería, solo cambies el código en un solo lugar (el método) 
        y no en todas las partes donde imprimas el dato.
    3)  Encapsulamiento Real: El usuario del objeto mi_dron no necesita saber cómo se 
        guarda la batería internamente; solo sabe que tiene dos "puertas" seguras para 
        interactuar con ella.
"""

class DronEntrega:
    def __init__(self, modelo, bateria_inicial):
        self.modelo = modelo                # Atributo Público
        self.__bateria = bateria_inicial    # Atributo Privado (Nadie debería tocar 
                                            # la batería directamente)

                                            # --- GETTER ---
    def obtener_bateria(self):              # Sirve para "leer" el valor privado desde fuera
        return f"Nivel de batería: {self.__bateria}%"

                                                # --- SETTER ---
    def establecer_bateria(self, nuevo_valor):  # Sirve para "modificar" el valor privado con REGLAS
        if 0 <= nuevo_valor <= 100:
            self.__bateria = nuevo_valor
            print(f"Batería actualizada a {self.__bateria}%")
        else:
            print("Error: El valor de batería debe estar entre 0 y 100.")



mi_dron = DronEntrega("SkyPhantom-X", 80)
print(f"Modelo: {mi_dron.modelo}")          # 1. Acceso al atributo público

                                            # 2. Intento de acceso directo al privado (Dará error)
# print(mi_dron.__bateria) # AttributeError

                                            # 3. Uso del GETTER para leer de forma segura
print(mi_dron.obtener_bateria())            # "Nivel de batería: 80%"

                                            # 4. Uso del SETTER para cambiar el valor con validación
mi_dron.establecer_bateria(95)              # Cambio exitoso
mi_dron.establecer_bateria(150)             # Bloqueado por la lógica del Setter

