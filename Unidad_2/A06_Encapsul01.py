""" el encapsulamiento suele ir de la mano con los métodos (para poder leer 
    o cambiar esos valores protegidos). Sin embargo, se puede explicar 
    perfectamente a nivel de atributos como una cuestión de "señalización" 
    y "seguridad de acceso".

    Explicación de forma muy visual y sencilla:
    ===========================================

    1.  El Concepto: "Público vs. Privado"
    -------------------------------------
    Imagina que una Clase es como una casa.
    1.1) Atributos Públicos: Son como el jardín o la fachada. Cualquiera que 
         pase por la calle puede verlos y tocarlos.
    1.2) Atributos Privados: Son como el contenido de tu caja fuerte o tu 
         diario personal. Están ahí, pero no quieres que nadie de fuera los
         manipule directamente.

    En Python, no existen las "puertas con llave" infranqueables, pero usamos 
    el guion bajo como señales de advertencia.

    ---------------------------------------------
    2. Los tres niveles de privacidad en Python
    ---------------------------------------------
    Usaremos como ejemplo una clase CuentaBancaria.

    A. PÚBLICO (SIN GUION BAJO)
    ---------------------------
    Es el estándar que hemos usado hasta ahora. Se puede ver y cambiar desde 
    cualquier parte.


            class Cuenta:
                def __init__(self, titular):
                    self.titular = titular # Público

            c1 = Cuenta("Juan")
            print(c1.titular)       # Se puede leer
            c1.titular = "Pedro"    # Se puede cambiar

    B. PROTEGIDO (UN GUION BAJO: _)
    -------------------------------
    Es una convención social. El guion bajo le dice al otro programador: 
    "Oye, este atributo es para uso interno de la clase, por favor no lo toques 
    desde afuera". Pero Python sí te deja acceder si insistes. Es como una señal
    de "No pasar".

            class Cuenta:
                def __init__(self, saldo_inicial):
                    self._saldo = saldo_inicial # Protegido (Señal de advertencia)

            c1 = Cuenta(1000)
            print(c1._saldo)            # Se puede leer, pero "está mal visto"

    C. PRIVADO / "OCULTO" (DOS GUIONES BAJOS: __)
    ---------------------------------------------
    Aquí Python se pone más serio. Cuando pones __, Python cambia el nombre del 
    atributo internamente para que sea difícil encontrarlo desde fuera. A esto 
    se le llama Name Mangling (Deformación de nombres).

            class Cuenta:
                def __init__(self, pin):
                    self.__pin = pin    # Privado (Caja fuerte)

            c1 = Cuenta(1234)
            # print(c1.__pin)           # ¡ERROR! Python dirá que no existe.

            
    3. ¿CÓMO "ROMPER" LA CAJA FUERTE? (PARA CURIOSOS)
    -------------------------------------------------
    Es importante decirle a los alumnos que en Python nada es 100% privado. Si 
    alguien realmente quiere entrar a __pin, puede hacerlo usando el nombre 
    deformado: 
    
                _NombreClase__atributo.


            print(c1._Cuenta__pin)  # Así sí podrías entrar, pero es una práctica 
                                    # prohibida en el trabajo real.

    Ejemplo Práctico: El Personaje de Videojuego
    Para tu clase, puedes usar este ejemplo que no usa métodos, solo atributos 
    para mostrar la diferencia de intención:
    
    Resumen:
    --------
     A) nombre      Público. "¡Úsame!"
     B) _nombre     Protegido. "No deberías usarme fuera de la clase".
     C) __nombre    Privado. "No me vas a encontrar fácilmente".
"""

class Personaje:
    def __init__(self, nombre, vida, id_secreto):
        self.nombre = nombre            # Público: Todos lo ven en la pantalla.
        self._vida = vida               # Protegido: Solo la lógica del juego debería tocarlo.
        self.__id_sistema = id_secreto  # Privado: Dato técnico que nadie debe ver.

p1 = Personaje("Arturo", 100, "USR-99")

print(p1.nombre)                        # "Arturo"
print(p1._vida)                         # Funciona, pero avisa que es interno.
print(p1._Personaje__id_sistema)        # Accede al atributo privado usando name mangling           .
