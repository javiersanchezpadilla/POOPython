""" MANEJO DE EXCEPCIONES.

    El tema de Excepciones es el puente entre el código que funciona en 
    condiciones ideales y el código que funciona en el mundo real.
    Manejar excepciones es como poner bolsas de aire y cinturones de seguridad 
    a los programas.
    
    El Flujo de una Excepción
    -------------------------
    Es vital visualizar qué pasa cuando algo sale mal. Normalmente, un error 
    rompe la ejecución y el programa muere. Con el manejo de excepciones, el 
    error es atrapado y procesado.
    
    Estructura de Control (La "Red de Seguridad")
    
    A)  try (Intentar): Aquí va el código que me da miedo que falle.
    B)  except (Atrapar): Si falló por esta razón específica, haz esto en 
        lugar de morir.
    C)  else (Si todo salió bien): Si no hubo ningún error, ejecuta esto.
    D)  finally (Pase lo que pase): No me importa si hubo error o no, esto se 
        tiene que hacer (como cerrar un archivo).
        
    Tipos de Errores Comunes en Ingeniería
    --------------------------------------
    No todos los errores son iguales. Es importante enseñarles a ser 
    específicos:
    
    Excepción               ¿Cuándo ocurre?                 Ejemplo práctico
    ValueError          El tipo de dato es correcto,    int("Hola") (No se 
                        pero el valor no.               puede convertir a 
                                                        número).
    ZeroDivisionError   División entre cero.            10 / 0
    FileNotFoundError   Se intenta abrir un archivo     open("datos_alum.txt")
                        que no existe.
    IndexError          Se accede a un índice fuera     lista = [1,2], intenta 
                        de rango en una lista.          ver lista[5].

    Ejemplo: Validación de Calificaciones
    -------------------------------------
    Vamos a crear un ejemplo para un sistema de la escuela. Queremos capturar 
    calificaciones, pero debemos asegurar que sean números y que estén entre 
    0 y 100.
"""
def capturar_calificacion():
    try:
        # El usuario podría escribir letras o números fuera de rango
        nota = float(input("Ingresa la calificación del alumno (0-100): "))
        
        if nota < 0 or nota > 100:
            # Forzamos un error manual si el rango es inválido
            raise ValueError("La calificación debe estar entre 0 y 100.")
            
    except ValueError as e:
        # Aquí atrapamos tanto si escribió letras como si el rango está mal
        print(f"Error de entrada: {e}")
    else:
        print(f"Calificación de {nota} registrada correctamente.")
    finally:
        print("Siguiente registro listo...")

# Prueba del sistema
capturar_calificacion()
