""" Dinamica para los alumnos: 
    ¿Qué datos de un usuario de una Red Social deberían ser públicos,
    protegidos o privados?

    Se trata de una tabla donde ellos deben decidir la "visibilidad" 
    de los datos de un usuario en una Red Social.

    -----------------------------------------------------------------------------------        
                                                                        Sugerencia 
    Atributo                ¿Quién debería tocarlo?                     de Formato
    -----------------------------------------------------------------------------------                                                                    
    Alias (Nickname)        Cualquier otro usuario que vea el perfil    self.alias
    Email                   Solo procesos internos .                    self._email
                            (como enviar notificaciones)
    Contraseña              Nadie, es un dato crítico del sistema.      self.__password
    Intentos de Login       Solo el sistema de seguridad de la app.     self.__intentos
    Biografía               El público en general.                      self.bio
    ID de Base de Datos     La infraestructura técnica del servidor.    self.__db_id

    Preguntas de reflexión para los alumnos:
    ----------------------------------------
    1)  ¿Por qué el _email sí se pudo leer pero el __password no?
        Porque el guion bajo simple es solo un aviso de "caballeros", mientras 
        que el doble guion bajo activa el "Name Mangling" que esconde el 
        nombre real.
    2)  Si el alias es público, ¿qué pasa si alguien lo cambia a "NombreOfensivo"?
        Como es público, cualquiera puede hacer user1.alias = "Malo". Aquí es donde 
        les puedes adelantar que en el futuro usaremos métodos para validar que 
        nadie ponga nombres prohibidos.
"""

class Usuario:
    def __init__(self, alias, email, password):
        self.alias = alias          # Público
        self._email = email        # Protegido
        self.__password = password  # Privado

user1 = Usuario("PythonMaster", "profe@mail.com", "123456")

# Intentos de acceso desde afuera de la clase:
                        # ✅ FUNCIONA
print(f"Viendo perfil de: {user1.alias}")      

                        # ⚠️ FUNCIONA (pero el guion bajo avisa que no deberías)
print(f"Correo de contacto: {user1._email}")   

                        # ❌ ERROR: AttributeError
print(f"Password: {user1.__password}")         