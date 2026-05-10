""" RAISE

    CREAR MIS PROPIOS TIPOS DE ERROR CON RAISE
    ------------------------------------------

    Consejos para usar raise
    -------------------------

    Consejo	                                    Explicación
    --------------------------------------------------------------------------
    Siempre usa mensajes claros	    En lugar de raise ValueError, usa raise 
                                    ValueError('La edad debe ser positiva')

    No abuses de raise	            No conviertas todo en excepción; usa 
                                    if/else para casos normales

    Sé específico con el tipo	    Usa ValueError para valores inválidos, 
                                    TypeError para tipos incorrectos, etc.

    Documenta qué excepciones 	    Usa comentarios o docstrings: Lanza 
    lanza tu función                ValueError si la edad es negativa

    Relanza solo cuando tenga 	    Si puedes manejar el error, hazlo. Si no, 
    sentido                         raise para que alguien más lo maneje

"""
# Creas tu propia clase de error
class SaldoInsuficienteError(Exception):
    pass

def retirar_dinero(saldo, cantidad):
    if cantidad > saldo:
        raise SaldoInsuficienteError(f"No puedes retirar {cantidad}. Saldo disponible: {saldo}")
    return saldo - cantidad

# Uso
try:
    nuevo_saldo = retirar_dinero(100, 150)
except SaldoInsuficienteError as e:
    print(f"Error bancario: {e}")
