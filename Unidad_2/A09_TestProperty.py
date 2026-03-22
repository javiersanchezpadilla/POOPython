""" 

#   Atributo            Tipo        Nivel de Acceso     Razón
--------------------------------------------------------------------
1   marca               String      Público         Información general
2   modelo              String      Público         Información general
3   color               String      Público         Se puede cambiar (repintar)
4   encendido           Bool        Público         Estado visible del coche
5   marcha_actual       Int         Público         Cambia constantemente
6   _kilometraje        Int         Protegido       No debería resetearse 
                                                    manualmente
7   _temperatura        Int         Protegido       Solo sensores internos lo 
                                                    modifican
8   __nivel_combustible Int         Privado         Requiere un Setter para no 
                                                    pasar de 100
9   __numero_serie      String      Privado         Identificador único e 
                                                    inmutable
10  __propietario       String      Privado         Requiere trámites legales 
                                                    para cambiarlo


    La estructura con 10 atributos, mezclando públicos, protegidos y privados,
    crear los accesos con @property.                                                    

"""
class Automovil:
    def __init__(self, marca, modelo, color, serie, combustible):
        # --- ATRIBUTOS PÚBLICOS (Se pueden ver y cambiar libremente) ---
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False      # Estado inicial
        self.marcha_actual = 0      # 0 = Neutral
        
        # --- ATRIBUTOS PROTEGIDOS (_) (Convención: No tocar desde fuera) ---
        self._kilometraje = 0       # Solo debe aumentar al conducir
        self._temperatura = 20      # Temperatura del motor en Celsius
        
        # --- ATRIBUTOS PRIVADOS (__) (Seguridad total con @property) ---
        self.__nivel_combustible = combustible  # 0 a 100%
        self.__numero_serie = serie             # Dato sensible (VIN)
        self.__propietario = "Agencia"          # Registro legal
