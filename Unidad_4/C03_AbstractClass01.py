""" CLASES ABSTRACTAS.

    Las Clases Abstractas son como el 'contrato legal' de la programación. 
    En ingeniería, las usamos cuando queremos definir una base común para 
    muchos objetos, pero no queremos que nadie pueda crear un objeto de esa 
    clase base porque está incompleta.

    Por ejemplo, puedes tener un Vehiculo, pero en la vida real no compras un 
    'vehículo' genérico, compras un Auto o una Moto. La clase Vehiculo es solo 
    el concepto (la clase abstracta).

    Para esto usamos el módulo abc (Abstract Base Classes) de Python.

    Aspectos clave de las Clases Abstractas:
    ----------------------------------------
    1)  No se pueden instanciar: Si intentas hacer v = Vehiculo(), Python dará 
        un error.
    2)  Métodos Abstractos: Son métodos que el padre define pero no programa. 
        Su única función es obligar a los hijos a programarlos.
    3)  Garantía de Polimorfismo: Aseguran que cualquier hijo, por ley, tendrá 
        los métodos necesarios para que el resto del sistema funcione.

    Ejemplo 1: El Sistema de Nómina.
    --------------------------------
    Imagina que en una empresa todos los empleados reciben un pago, pero el 
    cálculo es diferente según su contrato.
"""
from abc import ABC, abstractmethod

# 1. Definimos la clase abstracta (El Contrato)
class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        """Este método DEBE ser implementado por los hijos"""
        pass

# 2. Los hijos implementan su propia lógica
class EmpleadoFijo(Empleado):
    def calcular_salario(self):
        return 3000  # Salario mensual fijo

class EmpleadoPorHora(Empleado):
    def __init__(self, horas, tarifa):
        self.horas = horas
        self.tarifa = tarifa

    def calcular_salario(self):
        return self.horas * self.tarifa

# Prueba
# e = Empleado()  #<-- Esto daría ERROR
juan = EmpleadoFijo()
pedro = EmpleadoPorHora(40, 20)

print(f"Pago Juan: {juan.calcular_salario()}")
print(f"Pago Pedro: {pedro.calcular_salario()}")
