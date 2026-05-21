""" DECORADORES.

    Cómo se usa de la manera moderna (El símbolo @)
    -----------------------------------------------
    En lugar de hacer configuraciones raras, Python te permite aplicar el 
    decorador poniendo el símbolo @ justo arriba de la función que quieres 
    modificar.
"""
                            # 1. Definimos el decorador
def mi_decorador(funcion_original):
    
                            # 2. Creamos la funda o envoltura
    def envoltura():
        print("[Antes] Se va a ejecutar la función...")
        
        funcion_original()  # Aquí se ejecuta el código de la función original
        
        print("[Después] La función ha terminado de ejecutarse.\n")
        
                            # 3. Devolvemos la envoltura armada
    return envoltura

@mi_decorador
def abrir_puerta_laboratorio():
    print("El alumno escaneó su credencial y la puerta se abrió.")

@mi_decorador
def encender_proyector():
    print("El proyector del aula se ha encendido.")


                            # PROBAMOS LAS FUNCIONES
abrir_puerta_laboratorio()
encender_proyector()
