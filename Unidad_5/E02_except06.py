""" MANEJO DE EXCEPCIONES USANDO CLASES

    Aquí se presenta un escenario de Arquitectura Multicapa. En este ejemplo, 
    simularemos un Sistema de Procesamiento de Pagos para Inscripciones.

    La complejidad aquí radica en que las excepciones no solo validan datos 
    simples, sino que propagan errores entre diferentes métodos de una clase, 
    obligando a cada etapa a decidir si puede solucionar el problema o si debe 
    lanzar una excepción propia hacia la capa superior.

    Sistema de Validación de Transacciones Académicas
    -------------------------------------------------
    Este sistema tiene tres capas de validación:

    1)  Capa de Negocio: Valida que el monto sea coherente.
    2)  Capa de Integridad: Valida que los datos del cliente tengan el formato 
        correcto.
    3)  Capa de Ejecución: Es el bloque principal que coordina todo y maneja 
        los errores finales.

    ¿Qué hace a este ejemplo complejo?
    ----------------------------------
    1)  Propagación de Excepciones: En validar_monto, capturamos un error y 
        usamos raise para enviarlo a procesar_inscripcion. Esto enseña que los
        errores pueden viajar a través de los métodos hasta encontrar a 
        alguien que sepa qué hacer con ellos.
    2)  Múltiples tipos en un except: La línea except (ValueError, TypeError) 
        enseña que un solo bloque puede filtrar varias amenazas simultáneas si 
        el tratamiento va a ser similar.
    3)  Encadenamiento Lógico: El programa está diseñado para que, si el 
        SUB-BLOQUE A falla, el SUB-BLOQUE B nunca se ejecute. Esto es vital en 
        sistemas financieros o de bases de datos para mantener la integridad.
    4)  Uso de finally como auditoría: Sin importar si el pago fue exitoso o 
        falló por falta de saldo, el sistema genera un comprobante del intento. 
        Esto es una práctica estándar en ingeniería de software para auditoría 
        y logs (las bitacoras de registro de movimientos ;-).
"""
class ProcesadorPagos:
    def __init__(self, saldo_disponible):
        self.saldo_disponible = saldo_disponible

    def validar_monto(self, monto_str):
                                       # Capa 1: Conversión y coherencia lógica
        try:
            monto = float(monto_str)
            if monto <= 0:
                raise ValueError("El monto debe ser una cantidad positiva.")
            return monto
        # Re-lanzamos la excepción con un mensaje más específico para la
        # escuela
        except ValueError as e:
            
            raise ValueError(f"Falla en validación de monto: {e}")

    def validar_cliente(self, matricula):
                                        # Capa 2: Integridad de datos
        try:
            # La matrícula debe tener exactamente 8 dígitos (ejemplo del ITA)
            # (no estoy considerndo convalidaciones que son 9 digitos)
            if not (matricula.isdigit() and len(matricula) == 8):
                raise TypeError("Formato de matrícula inválido. Deben ser 8 dígitos.")
        except TypeError as e:
            raise e                     # Propagamos el error a la capa superior

    def procesar_inscripcion(self, matricula, monto_str):
                                        # Capa 3: Coordinación y ejecución del 
                                        # proceso completo
        print(f">>>> Iniciando proceso para matrícula: {matricula}")
        
                                        # SUB-BLOQUE A: Validación de datos de 
                                        # entrada
        try:
            self.validar_cliente(matricula)
            monto = self.validar_monto(monto_str)
            print("Datos de entrada validados correctamente.")
        except (ValueError, TypeError) as error_datos:
            print(f"Error en la recepción: {error_datos}")
            return                      # Detenemos este proceso, pero el 
                                        # programa sigue vivo

                                        # SUB-BLOQUE B: Lógica financiera (Saldo)
        try:
            if monto > self.saldo_disponible:
                                        # Excepción de lógica de negocio
                raise PermissionError("Fondos insuficientes en la cuenta del estudiante.")
            
            self.saldo_disponible -= monto
            print(f"Pago aprobado. Nuevo saldo: ${self.saldo_disponible}")
            
        except PermissionError as error_financiero:
            print(f"Transacción rechazada: {error_financiero}")
        
        finally:
            print("Generando comprobante de intento de operación...")


# PRUEBA DEL SISTEMA 
sistema = ProcesadorPagos(saldo_disponible=5000.0)

# Caso 1: Error de formato (Letras en monto)
sistema.procesar_inscripcion("20120987", "mil_pesos")

print("\n" + "="*40 + "\n")

# Caso 2: Error de lógica (Saldo insuficiente)
sistema.procesar_inscripcion("20120987", "6000.0")
