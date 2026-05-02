""" DISEÑO DE PATRONES STATE (ESTADO)

    Siguiente Patrón: State (Estado)
    ---------------------------------
    El patrón State permite que un objeto cambie su comportamiento cuando su 
    estado interno cambia. El objeto parecerá que ha cambiado de clase.

    Ejemplo clásico: Un cajero automático. El botón 'Retirar' se comporta 
    diferente si el cajero tiene dinero, si no tiene, o si la tarjeta está 
    bloqueada.

    Patrón de Comportamiento: State (Estado)
    ----------------------------------------
    **) El Problema: El comportamiento de un objeto depende de su estado y 
        debe cambiar en tiempo de ejecución. Si intentas programar esto con 
        condiciones simples, terminas con un código espagueti difícil de 
        mantener.
    **) La Solución: Extraer cada estado en una clase separada. El objeto 
        principal (llamado Contexto) delega el trabajo al objeto de estado 
        actual. Cuando el estado cambia, el contexto simplemente apunta a un 
        objeto de estado diferente.

    Ejemplo: El Proceso de un Pedido (E-commerce)
    ---------------------------------------------
    Un pedido puede estar en estado: Pendiente, Pagado o Enviado. El 
    comportamiento del botón 'Cancelar' es distinto en cada estado.

    Por qué es Ingeniería de Calidad:
    ---------------------------------
    1)  Principio de Responsabilidad Única: Cada estado tiene su propia lógica. 
        Si el proceso de reembolso cambia, solo tocas la clase EstadoPagado.
    2)  Adiós a los condicionales: El objeto Pedido no tiene un solo if para 
        decidir qué hacer; el polimorfismo hace el trabajo sucio.
    3) Extensibilidad: Si mañana la empresa añade un estado 'En Aduana', solo 
        creamos una clase nueva y el resto del código sigue funcionando igual.
"""
from abc import ABC, abstractmethod

# 1. Interfaz de Estado
class EstadoPedido(ABC):
    @abstractmethod
    def cancelar(self):
        pass

# 2. Estados Concretos
class EstadoPendiente(EstadoPedido):
    def cancelar(self):
        return "Pedido cancelado con éxito. No se realizó ningún cargo."

class EstadoPagado(EstadoPedido):
    def cancelar(self):
        return "Cancelando... Se procesará un reembolso a tu tarjeta."

class EstadoEnviado(EstadoPedido):
    def cancelar(self):
        return "Error: El pedido ya está en camino. No se puede cancelar."

# 3. El Contexto (El Pedido)
class Pedido:
    def __init__(self):
        # Estado inicial
        self._estado = EstadoPendiente()

    def cambiar_estado(self, nuevo_estado: EstadoPedido):
        self._estado = nuevo_estado
        print(f"--- El estado del pedido ha cambiado a: {type(nuevo_estado).__name__} ---")

    def presionar_boton_cancelar(self):
        # El pedido no sabe cómo cancelar, le pregunta a su estado actual
        print(self._estado.cancelar())

# --- PRUEBA DE LA MÁQUINA DE ESTADOS ---

mi_pedido = Pedido()

# Caso 1: Pendiente
mi_pedido.presionar_boton_cancelar()

# Caso 2: Pagado
mi_pedido.cambiar_estado(EstadoPagado())
mi_pedido.presionar_boton_cancelar()

# Caso 3: Enviado
mi_pedido.cambiar_estado(EstadoEnviado())
mi_pedido.presionar_boton_cancelar()
