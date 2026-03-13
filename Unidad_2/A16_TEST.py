""" El Enunciado para los Alumnos:

    Instrucciones: En equipos, desarrollen la clase Heroe que cumpla con:
    ---------------------------------------------------------------------
    1)  Al crear un héroe, el contador de la clase debe aumentar en 1.
    2)  Si no se define un poder al crear al héroe, este debe ser por defecto
        "Fuerza Humana".
    3)  Protejan la identidad_secreta para que no sea modificable después de 
        crear al héroe (solo lectura).
    4)  Aseguren que la energia (inicia en 100) nunca sea negativa. Si alguien 
        intenta ponerle -10, el sistema debe dejarla en 0.
    5)  Creen un método encadenable .recibir_danio(cantidad) que reste energía 
        y permita seguir configurando al héroe en la misma línea.
    6)  Crear un método encadenable entrenar(), de modo que puedan hacer: 
        h1.entrenar().entrenar().entrenar() para sumar energia al heroe.
    7)  Creen un método para impresión de la información del heroe, que muestre
        el nombre del héroe y su nivel de energía.

    Cronograma Sugerido (50 min):
    -----------------------------
    A)  00-10 min: Lectura y diseño de la estructura (identificar qué es privado y
        qué es público).
    B)  10-35 min: Codificación de la clase, constructor y decoradores @property.
    C)  35-45 min: Pruebas de error (intentar poner energía negativa o cambiar la 
        identidad).
    D)  45-50 min: Demostración rápida al profesor.

    ¿Por qué este problema es efectivo?
    -----------------------------------
    A)  Getters/Setters: Los obliga a usar @property para la validación de la 
        energía.
    B)  Atributos de Clase: El contador total_heroes es el ejemplo clásico para 
        entender la diferencia entre "lo que es de la clase" y "lo que es del objeto".
    C)  Parámetros por ausencia: Evita errores si el usuario olvida pasar todos los 
        datos al crear el objeto.

    Instrucciones de aplicación para ti:
    ------------------------------------
    1)  El "Hack" de Identidad: Diles que intenten cambiar la identidad con 
        h1.identidad_secreta = "Nuevo Nombre". Si el código les lanza un 
        AttributeError, ¡felicidades!, implementaron correctamente un atributo de 
        solo lectura.
    2)  Validación de Energía: Pídeles que impriman el objeto después de intentar 
        ponerle -100 de energía. Si el programa muestra 0%, la lógica del Setter 
        es correcta.
    3)  Contador Global: Al final, deben crear al menos dos objetos y verificar
        que Heroe.total_heroes sea igual a 2. Esto confirma que entienden los 
        atributos de clase.

    ✅ Guía de Revisión Rápida (Solucionario)
    -----------------------------------------
    1.  El Atributo de Clase (Contador)
        Qué revisar: Que esté fuera del __init__ y que se acceda a él usando el 
        nombre de la clase.
            *) Correcto: Heroe.total_heroes += 1
            *) Error común: self.total_heroes += 1 (Esto crearía un atributo de 
               instancia en lugar de afectar al contador global).

    2.  Encapsulamiento (Atributos Privados)
        Qué revisar: El uso del doble guion bajo (__).
            *) Correcto: self.__energia y self.__identidad_secreta.
            *) Por qué importa: Si solo usan un guion (_), es una convención de 
               "protegido", pero el doble guion activa el Name Mangling de Python, 
               que es lo que realmente evaluamos en encapsulamiento estricto.

    3.  La Lógica del Setter (El corazón del reto)
        Qué revisar: Que el setter maneje los límites (0 y 100).
                @energia.setter
                def energia(self, valor):
                    if valor < 0:
                        self.__energia = 0
                    elif valor > 100:
                        self.__energia = 100
                    else:
                        self.__energia = valor

    Punto extra: Si el alumno usó las funciones max() y min() para simplificar
    la lógica: self.__energia = max(0, min(100, valor)) (Esto demuestra un nivel 
    avanzado de Python).

    4)  4. Parámetro por Ausencia
        Qué revisar: Que el constructor tenga el valor por defecto en el lugar 
        correcto (al final).                               vvvvvvvvvvvvvvvvvvvvv
        *) Correcto: def __init__(self, nombre, identidad, poder="Fuerza Humana"):
        *) Error: Poner el parámetro con valor por defecto antes de uno obligatorio. 
           Python lanzará un SyntaxError.

    Tabla de puntuación sugerida:

    Concepto            Valor           Indicador de éxito
    Constructor         20%         Usa correctamente self y asigna los 
                                    parámetros obligatorios y opcionales.
    Atributo Clase      15%         El contador sube con cada nueva instancia 
                                    de Heroe.
    Getters (@property) 20%         Permite leer la identidad y la energía sin 
                                    acceder directamente al __.
    Setter (@setter)    25%         El código no explota si pones energía -50; 
                                    se ajusta a 0 automáticamente.
    Método entrenar     10%         Modifica la energía correctamente usando la 
                                    propiedad, debe ser encadenable.
    Mét recibir_danio   10%         Permite restar la energia del heroe, debe ser
                                    encadenable.

    Formato (str)       10%         Al hacer print(objeto) se ve la información 
                                    limpia y legible.

                                    
    Señales de Alerta (Errores Críticos)
    ====================================
    1)  Recursión Infinita: Si dentro del setter de energía escriben 
        self.energia = valor en lugar de self.__energia = valor, el programa entrará 
        en un bucle infinito y se detendrá con un RecursionError. Es el error más 
        común al aprender @property.
    2)  Identidad Modificable: Si crearon un @identidad_secreta.setter, han fallado el 
        requerimiento de "Solo lectura".

    ¿Qué decirles al terminar?
    --------------------------
    'Hoy no solo crearon un objeto, crearon una interfaz segura. Gracias al encapsulamiento, 
    no importa quién use su clase Heroe, nunca podrán dejarlo con energía negativa ni descubrir 
    su identidad por error. Eso es software de calidad.'

"""

class Heroe:
    # --- 1. ATRIBUTOS DE CLASE ---
    # TODO: Crear un contador llamado 'total_heroes' que inicie en 0
    total_heroes = 0

    def __init__(self, nombre, identidad, poder="Fuerza Humana"):
        # --- 2. ATRIBUTOS DE INSTANCIA ---
        self.nombre = nombre
        self.poder = poder
        
        # TODO: Hacer que estos dos sean PRIVADOS
        self.__identidad_secreta = identidad
        self.__energia = 100
        
        # TODO: Incrementar el contador de la clase cada que se crea un objeto
        Heroe.total_heroes += 1

    # --- 3. GETTERS Y SETTERS (@property) ---

    # TODO: Crear un Getter para 'identidad_secreta' (Solo lectura)
    @property
    def identidad_secreta(self):
        return f"Top Secret: {self.__identidad_secreta}"

    # TODO: Crear un Getter y un Setter para 'energia'
    # El setter debe validar que la energía esté entre 0 y 100
    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, valor):
        if valor < 0:
            self.__energia = 0
        elif valor > 100:
            self.__energia = 100
        else:
            self.__energia = valor

    # --- 4. MÉTODOS DE LA CLASE ---

    def entrenar(self):
        """Aumenta la energía en 10 usando el setter."""
        print(f"{self.nombre} está entrenando...")
        # TODO: Sumar 10 a la energía usando el setter
        self.energia += 10
        return self # Para permitir encadenamiento si lo desean

    def hacer_danio(self):
        """Disminuye la energía en 10 usando el setter."""
        print(f"{self.nombre} está perdiendo energia...")
        # TODO: Restar 10 a la energía usando el setter
        self.energia -= 10
        return self # Para permitir encadenamiento si lo desean


    def muestra_heroe(self):
        """Muestra el estado actual del héroe."""
        return f"HÉROE: {self.nombre} | Poder: {self.poder} | Energía: {self.energia}%"

# --- BLOQUE DE PRUEBAS (El alumno debe descomentar esto para verificar) ---
h1 = Heroe("Capitán Python", "Guido Van Rossum", "Código Infinito")
h2 = Heroe("Ultra Java", "James Gosling")   # Aquí se aplica parámetro por ausencia

print(h1.muestra_heroe())
h1.energia = -50                            # Debería ajustarse a 0
h1.entrenar().entrenar().entrenar()         # Debería subir a 10
print(h1.muestra_heroe())
h1.hacer_danio().hacer_danio()
print(h1.muestra_heroe())
print(f"Identidad: {h1.identidad_secreta}")
print(f"Héroes registrados: {Heroe.total_heroes}")
