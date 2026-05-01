""" PATRONES DE DISEÑO (OBSERVER)

    2. Observer (Patrón de Comportamiento)
    --------------------------------------
    Problema: Necesitas que varios objetos se enteren automáticamente cuando 
    un objeto principal (el 'Sujeto') cambia su estado. No quieres que el 
    Sujeto esté preguntando uno por uno a los demás, porque eso crearía un 
    acoplamiento muy fuerte.

    Solución: El Sujeto mantiene una lista de 'Observadores'. Cuando el Sujeto 
    cambia, les envía una notificación a todos los de la lista. Es el sistema 
    de 'Suscripción'.

    Ejemplo: Sistema de Notificaciones de YouTube

    ¿Por qué enseñar estos dos juntos?
    
    Patrón              Enfoque Ingenieril                  AnalogíA
    --------------------------------------------------------------------------
    Factory Method  Desacopla la creación. El       Como un menú de restaurante
                    código no depende de nombres    tú pides 'Pasta' y la 
                    de clasesespecíficas            cocina decide si es
                                                    Fettuccine o Penne según 
                                                    el día.
    Observer        Desacopla la comunicación.      Como una alarma de 
                    El objeto principal no          incendios: la alarma no 
                    necesita saber quiénes lo       sabe quién está en el 
                    escuchan.                       edificio, solo suena y 
                                                    quienes estén suscritos 
                                                    (cerca) reaccionan.

    Pedir a los alumnos el siguiente cambio:
    ----------------------------------------
    1)  Usar una Fábrica para crear diferentes tipos de sensores (Temperatura,
        Humedad).
    2)  Usar el patrón Observer para que una central de alarmas 'escuche' a 
        todos esos sensores y avise si alguno detecta un valor crítico.
"""                 
class CanalYouTube:
    def __init__(self, nombre):
        self.nombre = nombre
        self.suscriptores = [] # Lista de observadores

    def suscribir(self, usuario):
        self.suscriptores.append(usuario)

    def subir_video(self, titulo):
        print(f"\n{self.nombre} ha subido: '{titulo}'")
        self._notificar_suscriptores(titulo)

    def _notificar_suscriptores(self, titulo):
        for s in self.suscriptores:
            s.update(self.nombre, titulo)

# Interfaz Observador
class Suscriptor:
    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    def update(self, canal, video):
        print(f"Hola {self.nombre_usuario}, el canal {canal} subió un nuevo video: {video}")

# Prueba
canal_tecnologia = CanalYouTube("Cómputo ITA")
user1 = Suscriptor("Javier")
user2 = Suscriptor("Estudiante_Sistemas")

canal_tecnologia.suscribir(user1)
canal_tecnologia.suscribir(user2)

canal_tecnologia.subir_video("Tutorial de Patrones de Diseño")
