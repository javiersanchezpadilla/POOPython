""" DECORADORES

    EjemplO: El decorador de Bitácora (Logger)
    ------------------------------------------
    En el desarrollo profesional de sistemas, los decoradores se usan 
    muchísimo para crear auditorías (saber quién hizo qué y a qué hora) o para 
    medir el rendimiento del software.

    Decorador práctico que registra en una lista de auditoría cada vez que se 
    ejecuta una operación matemática crítica:

    
    ¿Por qué usar los decoradores?
    ------------------------------
    1)  Reutilización de código (DRY - Don't Repeat Yourself): Escribes el 
        código de seguridad o de medición una sola vez en el decorador y se lo 
        puedes aplicar a 100 funciones diferentes usando solo la etiqueta @.
    2)  Separación de responsabilidades: Tu función principal se enfoca 
        únicamente en su tarea (por ejemplo, calcular una calificación), 
        mientras que el decorador se encarga de las tareas secundarias 
        (guardar logs, verificar contraseñas, medir tiempos). Tu arquitectura 
        se vuelve limpia y modular.
"""
bitacora_operaciones = []

def auditoria(funcion_original):
    def envoltura(*args, **kwargs):
                            # Guardamos en nuestra bitácora la acción antes 
                            # de ejecutarla
        mensaje = f"Examen de POO: Se invocó la función '{funcion_original.__name__}' con los valores {args}"
        bitacora_operaciones.append(mensaje)
        
                            # Ejecutamos la operación original
        return funcion_original(*args, **kwargs)
    return envoltura

                            # Decoramos múltiples funciones con el mismo 
                            # auditor
@auditoria
def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3

@auditoria
def aplicar_descuento_beca(pago_original):
    return pago_original * 0.5

                            # Ejecutamos código común de nuestra app
calcular_promedio(90, 85, 100)
aplicar_descuento_beca(1500)

                            # Revisamos cómo quedó nuestra bitácora automatizada
print("REGISTROS DE AUDITORÍA DEL SISTEMA:")
for registro in bitacora_operaciones:
    print(f" -> {registro}")
