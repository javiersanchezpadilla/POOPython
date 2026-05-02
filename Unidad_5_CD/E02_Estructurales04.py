""" PATRONES DE DISEÑO ESTRUCTURALES (PROXY)

    patrón Proxy, que también es estructural y sirve para poner un 
    'guardaespaldas' frente a un objeto.

    El patrón Proxy es sumamente interesante porque introduce el concepto de 
    intermediario. En lugar de hablar directamente con el objeto 'real', 
    hablamos con un representante (el Proxy) que decide si nos deja pasar o no.

    Patrón Estructural: Proxy (Sustituto)
    -------------------------------------
    A)  El Problema: A veces tenemos un objeto que consume muchos recursos 
        (memoria, red, tiempo) o que es muy sensible (seguridad). No queremos 
        que cualquier parte del programa acceda a él directamente o que se 
        cargue en memoria si no es estrictamente necesario.
    B)  La Solución: Crear un objeto escudo que tiene la misma interfaz que el 
        objeto real. El cliente no sabe que está hablando con un Proxy. 
        El Proxy controla el acceso y solo cuando es necesario, llama al 
        objeto real.

    Ejemplo: El Proxy de Seguridad (Control de Acceso)
    --------------------------------------------------
    Imagina que tenemos una base de datos con información sensible. Solo los 
    usuarios con el rol de Administrador pueden realizar cambios.

"""
from abc import ABC, abstractmethod

# Interfaz común
class ServicioDatos(ABC):
    @abstractmethod
    def consultar_nomina(self, usuario):
        pass

# Objeto Real (Sensible y pesado)
class BaseDeDatosReal(ServicioDatos):
    def consultar_nomina(self, usuario):
        print(f"--- Accediendo a disco... Obteniendo nómina para {usuario} ---")
        return "$50,000 MXN"

# PROXY de Seguridad
class ProxySeguridad(ServicioDatos):
    def __init__(self, base_real):
        self._base_real = base_real
        self._usuarios_autorizados = ["Javier", "Admin_Sistemas"]

    def consultar_nomina(self, usuario):
        if usuario in self._usuarios_autorizados:
            # Si está autorizado, le pasamos la petición al objeto real
            return self._base_real.consultar_nomina(usuario)
        else:
            # Si no, bloqueamos el acceso
            return "ACCESO DENEGADO: No tienes permisos suficientes."

# --- USO ---
db_real = BaseDeDatosReal()
escudo = ProxySeguridad(db_real)

print(escudo.consultar_nomina("Estudiante123")) # Bloqueado
print(escudo.consultar_nomina("Javier"))        # Permitido
