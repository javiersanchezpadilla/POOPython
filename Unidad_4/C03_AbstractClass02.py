""" CLASES ABSTRACTAS.

    jemplo 2: Armas en un Videojuego (Aplicado)
    -------------------------------------------
    Queremos que todas las armas tengan un método disparar, pero el 'arma 
    genérica' no sabe cómo disparar.

    ¿Por qué enseñar esto en Ingeniería?
    Evita errores de ejecución: Es mejor que el programa falle al inicio 
    porque un programador olvidó un método, a que falle en medio del juego 
    cuando el usuario presiona 'disparar'.

    Trabajo en Equipo: DiseñaR la clase abstracta Enemigo, que los estudiantes
    pueden crear 20 tipos de enemigos distintos, así tendre la seguridad de 
    que todos tendrán los métodos mover() y morir() porque @abstractmethod 
    fueron obligados-

    Resumen para los alumnos:
    -------------------------
    'Una Clase Abstracta es un plano que dice qué debe tener una casa, pero no 
    es una casa en la que puedas vivir. Solo cuando construyes una casa real 
    (Subclase) basándote en ese plano, puedes entrar en ella.'

    SOLUCIÓN

            class Arco(Arma):
            
            def disparar(self):                 <-- Debe agregar el método 
                print("zas por el aire")

        arco = Arco()
        arco.disparar()
"""
from abc import ABC, abstractmethod

class Arma(ABC):
    @abstractmethod
    def disparar(self):
        pass

class Pistola(Arma):
    def disparar(self):
        print("¡Piu! ¡Piu!")

class Lanzallamas(Arma):
    def disparar(self):
        print("¡FIIIIIIIIIIISH!")

# Si un alumno intenta crear esto y olvida el método disparar...
class Arco(Arma):
    pass 


arco = Arco()
arco.disparar()
# Python dará ERROR: "Can't instantiate abstract class Arco with 
# abstract method disparar"
# arco = Arco()  
                
