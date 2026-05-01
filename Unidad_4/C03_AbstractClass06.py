""" CLASES ABSTRACTAS (HERENCIA DE OBLIGACIONES)

    SI UNA CLASE HEREDA DE UNA CLASE ABSTRACTA PERO NO IMPLEMENTA TODOS SUS 
    MÉTODOS ABSTRACTOS, ESA CLASE HIJA TAMBIÉN SE VUELVE ABSTRACTA Y PYTHON NO
    TE DEJARÁ CREAR OBJETOS DE ELLA TAMPOCO. ES UNA 'HERENCIA DE OBLIGACIONES'.

    LAS CLASES ABSTRACTAS OBLIGAN EL POLIMORFISMO.

    Este es un escenario excelente para explicar la 'Herencia de Obligaciones'. 
    En ingeniería de software, esto se usa cuando vamos especializando un 
    concepto poco a poco, pero el objeto sigue sin estar 'completo' para 
    existir en el mundo real hasta llegar a un nivel muy específico.

    Vamos a usar el ejemplo de un Sistema de Dispositivos Electrónicos.
    El Escenario:
    1)  Nivel 1 (Abuelo): Dispositivo (Abstracto). Define que todo dispositivo 
        debe encender y configurar.
    2)  Nivel 2 (Padre): DispositivoInalambrico (Sigue siendo Abstracto). 
        Implementa configurar (porque todos los inalámbricos se configuran 
        igual conectándose al Wi-Fi), pero no implementa encender.
    3)  Nivel 3 (Hijo): SmartWatch (Concreto). Finalmente implementa encender.

    Una vez ejecutado el programa se tiene que entender lo siguiente:
    -----------------------------------------------------------------
    ¿Por qué falló el Nivel 2?
    Aunque DispositivoInalambrico es más específico que Dispositivo, todavía 
    tiene una 'deuda' pendiente: el método encender. En Python, si heredas de 
    una clase abstracta y dejas aunque sea un solo @abstractmethod sin definir, 
    tú también te vuelves abstracto por 'contagio'.

    La Acumulación de Responsabilidades:
    La clase SmartWatch tiene éxito porque no solo hace su trabajo (encender), 
    sino que también se beneficia del trabajo que ya hizo su padre 
    (configurar_wifi).

    Utilidad en Ingeniería:
    Esto permite crear familias de productos. Puedes tener una clase 
    intermedia Smartphone que implemente métodos comunes a todos los teléfonos
    y luego clases concretas como iPhone o Galaxy que solo implementen los 
    detalles finales de su hardware.

    Reflexión:
    Este modelo jerárquico es la forma más pura de Arquitectura Orientada a 
    Objetos. Asegura que el programador final no tenga que escribir todo 
    desde cero, pero le prohíbe dejar el trabajo a medias.

    las Clases Abstractas no son un estorbo, sino una red de seguridad.

    Al obligar a la adaptación de las clases, el polimorfismo deja de ser algo 
    que 'podría' funcionar y se convierte en algo que garantizadamente 
    funciona.

    ¿Por qué este enfoque les da una visión total?
    ----------------------------------------------
    1)  Elimina el miedo al error en tiempo de ejecución: Sin clases 
        abstractas, un alumno podría crear una lista de objetos y, a mitad de 
        la exposición del proyecto, el programa 'tronar' porque a una clase 
        le faltaba un método. Con este modelo, Python ni siquiera los deja 
        arrancar si el contrato no está firmado.
    2)  Desacoplamiento Real: Les permite entender que pueden diseñar un 
        'Cargador de Dispositivos' que solo reciba objetos de tipo Dispositivo. 
        No le importa si es un SmartWatch o un Smartphone; el cargador confía 
        ciegamente en que el método encender() existe.
    3)  Jerarquía de Especialización: Les enseña que la programación es como 
        la taxonomía biológica: vamos de lo general (Inalámbrico) a lo 
        específico (SmartWatch), y solo lo específico tiene 'vida' propia 
        (instanciación).

    'En un equipo de desarrollo profesional, el Arquitecto de Software escribe 
    las Clases Abstractas para definir qué debe hacer el sistema, y los 
    Programadores escriben las Clases Concretas para definir cómo lo hace cada 
    parte. El polimorfismo es el pegamento que permite que el trabajo de todos 
    se una sin conflictos.'
"""
from abc import ABC, abstractmethod

# NIVEL 1: LA BASE TOTALMENTE ABSTRACTA
class Dispositivo(ABC):
    def __init__(self, marca):
        self.marca = marca

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def configurar_wifi(self):
        pass

# NIVEL 2: CLASE INTERMEDIA (SIGUE SIENDO ABSTRACTA)
# Al NO implementar 'encender()', esta clase HEREDA la abstracción.
# Python NO permitirá crear objetos de 'DispositivoInalambrico'.
class DispositivoInalambrico(Dispositivo):
    # Esta clase implementa UNO de los métodos abstractos
    def configurar_wifi(self):
        print(f"Buscando redes para el dispositivo {self.marca}...")
        print("Conectado exitosamente al Wi-Fi de la facultad.")
    
    # Aquí tendría que ir la implementación del método encender()
    

# NIVEL 3: CLASE FINAL (CONCRETA)
class SmartWatch(DispositivoInalambrico):
    # Finalmente, implementamos el método que faltaba
    def encender(self):
        print(f"Pantalla OLED de {self.marca} iluminada. Iniciando sistema...")


# Creación de las instancias
print("Intentando crear objetos...")

# 1. Intento con el Abuelo (Falla)
# d = Dispositivo("Generic") # Error: Can't instantiate abstract class

# 2. Intento con el Padre (Falla porque le falta 'encender')
# padre = DispositivoInalambrico("Router Linksys")


reloj = SmartWatch("Apple")
print(f"\nÉxito en Nivel 3:")
reloj.encender()        # Implementado en Nivel 3
reloj.configurar_wifi() # Implementado en Nivel 2
