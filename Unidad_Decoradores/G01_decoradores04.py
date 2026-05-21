""" DECORADORES

    Funciones que reciben parámetros (*args y kwargs)
    -------------------------------------------------
    El ejemplo anterior funciona bien para funciones vacías, pero ¿qué pasa si 
    la función que queremos decorar recibe argumentos (como el nombre de un 
    alumno o calificaciones)?

    Para que la envoltura sea universal y acepte cualquier tipo de parámetro, 
    usamos *args (argumentos por posición) y kwargs (argumentos por nombre).

    Imaginemos un decorador de seguridad que simula la validación de un 
    usuario administrador antes de permitirle hacer una acción:
"""
def requiere_admin(funcion_original):
    def envoltura(*args, **kwargs):
        # Simulamos una comprobación de seguridad extra
        print("[SEGURIDAD] Verificando credenciales en el sistema...")
        
        # Ejecutamos la función pasando todos los argumentos que traía originalmente
        resultado = funcion_original(*args, **kwargs)
        
        return resultado
    return envoltura

# Aplicamos el decorador a una función con parámetros
@requiere_admin
def registrar_calificacion(nombre_alumno, nota):
    print(f"Éxito: Se registró {nota} para el alumno {nombre_alumno}.")

# Prueba del sistema
registrar_calificacion("Javier", 100)
