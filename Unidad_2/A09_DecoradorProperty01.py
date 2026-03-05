""" Decorador property

    El uso de @property es lo que diferencia a un programador que viene de 
    otros lenguajes (como Java) de un verdadero Pythonista.
    En Python, amamos la limpieza. El @property nos permite usar Getters y 
    Setters pero con una sintaxis que parece un atributo normal 
    (sin paréntesis ()), lo que hace que el código sea mucho más elegante.

    El problema: ¿Por qué usar @property?
    -------------------------------------
    Si usamos los Getters y Setters tradicionales (get_precio()), el 
    usuario de tu clase tiene que escribir mucho. Con @property, el 
    usuario simplemente escribe '.precio', pero por detrás se ejecutan tus 
    reglas de seguridad.

    Ejemplo Práctico: Clase Producto
    Imagina que tenemos un producto. No queremos que el precio sea negativo y 
    queremos que, al leerlo, siempre nos muestre el símbolo de moneda.

    Las 3 partes clave del @property
    --------------------------------

    Para que tus alumnos no se confundan, diles que busquen estos tres elementos:
    **) El atributo "oculto" (self._precio): Es donde realmente guardamos el dato.
    **) El Decorador @property: Es el Getter. Se llama igual que el atributo que 
        queremos simular.
    **) El Decorador @nombre.setter: Es el Setter. Permite usar el signo = para 
        asignar valores y validarlos.

    Ventajas de este estilo (Nivel Intermedio)
    ------------------------------------------
    **) Compatibilidad: Si empezaste con un atributo público self.precio y luego 
        decides que necesita reglas de seguridad, puedes convertirlo en @property 
        sin romper el código de las personas que ya usaban tu clase.

    **) Atributos de "Solo Lectura": Si creas un @property pero no creas su .setter,
        el atributo se vuelve imposible de cambiar desde fuera.
        =============================================================================+

    SINTAXIS:
    Cuando creamos la propiedad (nombre_propiedad), lo que está abajo de @property, 
    deberá seguir usandose el mismo nombre para el setter, esto es, que el setter
    se debe declarar @nombre_propiedad.setter, y el método asociado tambien debe
    tener el nombre de la propiedad (nombre_propiedad)

    class Sintaxis:

        def __init__(self, atributo):
            self._atributo = atributo   <-- Atributo no público declarado

    @property
    def <nombre_propiedad>(self):       <-- Creación de la propiedad 'nombre_propiedad'
        return self._atributo           <-- retornamos el atributo protegido

                                        <-- usamos el mismo nombre de arriba
    @nombre_propiedad.setter            <-- @nombre_propiedad.setter
    def <nombre_propiedad>(self, nuevo_valor_atributo): <-- La fn se debe llamar igual
        self._atributo = nuevo_valor_atributo

"""

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre        # púublico
        self._precio = precio       # privado

    @property                       # GETTER (Decorado con @property)
    def precio(self):
        print("-> Accediendo al precio de forma segura...")
        return f"${self._precio:,.2f}"

    @precio.setter                  # SETTER (Decorado con @nombre_metodo.setter)
    def precio(self, nuevo_valor):
        if nuevo_valor > 0:
            print(f"-> Cambiando precio a {nuevo_valor}...")
            self._precio = nuevo_valor
        else:
            print("Error: El precio no puede ser cero o negativo.")


p1 = Producto("Monitor", 2500)

                        # Lo usamos como un atributo normal (SIN PARÉNTESIS)
print(p1.precio)        # Ejecuta el Getter: "$2,500.00"

                        # Intentamos cambiarlo como un atributo normal
p1.precio = 3000        # Ejecuta el Setter: Cambia el valor
p1.precio = -500        # Ejecuta el Setter: Bloquea el cambio
