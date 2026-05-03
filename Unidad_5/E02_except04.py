""" MANEJO DE EXCEPCIONES USANDO CLASES

    Validador de Base de Datos de Estudiantes
    -----------------------------------------
    Este ejemplo muestra cómo validar un formato de correo y luego intentar 
    una inserción lógica.
"""
class RegistroEstudiante:
    def registrar(self, correo):
                                        # Validación de formato
        try:
            if "@" not in correo:
                raise NameError("Correo institucional inválido.")
            print("Formato de correo verificado.")
        except NameError as e:
            print(f"Validación fallida: {e}")
            return

                                        # Simulación de guardado
        try:
            # Simulamos que la base de datos está llena
            db_llena = True
            if db_llena:
                raise OverflowError("Memoria de base de datos llena.")
            print("Estudiante guardado en el sistema.")
        except OverflowError as e:
            print(f"Error de almacenamiento: {e}")

registro = RegistroEstudiante()
registro.registrar("alumno.acapulco.tecnm.mx")     # Forzará el primer bloque
