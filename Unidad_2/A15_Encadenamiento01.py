""" ENCADENAMIENTO DE MÉTODOS.

    ENCADENAMIENTO DE MÉTODOS EN PYTHON (o Method Chaining en inglés) es una 
    técnica de programación que permite enlazar múltiples llamadas a métodos 
    sobre un mismo objeto en una sola expresión. En otras palabras, es como 
    construir una cadena de acciones que se ejecutan secuencialmente sobre un 
    objeto, haciendo que el código sea más conciso y elegante.

    ¿CÓMO FUNCIONA?
    ---------------
    Para que el encadenamiento de métodos funcione, cada método en la cadena 
    debe retornar el objeto sobre el que se ha invocado. De esta manera, el 
    resultado de un método se convierte automáticamente en el objeto sobre el 
    que se aplicará el siguiente método.

            Ejemplo:
            texto = "  Hola, mundo!  "
            resultado = texto.strip().upper().split()

    En este ejemplo:
    1)  texto.strip() elimina los espacios en blanco al inicio y al final de la 
        cadena, Toma el string original, le quita los espacios y devuelve un 
        nuevo string ("Hola, mundo!").
    2)  upper() convierte todas las letras a mayúsculas, Se ejecuta sobre el 
        resultado anterior. Convierte el texto a mayúsculas y devuelve otro 
        string ("HOLA, MUNDO!").
    3)  split() divide la cadena en una lista de palabras, Se ejecuta sobre el 
        string en mayúsculas. Corta el texto por los espacios y devuelve una 
        lista (['HOLA,', 'MUNDO!']).

    Todo esto se logra en una sola línea, gracias al encadenamiento de métodos.

    VENTAJAS DEL ENCADENAMIENTO DE MÉTODOS:
    ---------------------------------------
    **) Mayor legibilidad: El código se vuelve más fácil de leer y entender, ya 
        que se expresa de manera más natural, como si estuvieras describiendo 
        una secuencia de acciones.
    **) Menos variables intermedias: Al no ser necesario crear variables para 
        almacenar los resultados intermedios de cada método, se reduce la cantidad 
        de código y se mejora la eficiencia.
    **) Estilo funcional: Se alinea con el estilo de programación funcional, que 
        promueve la inmutabilidad y la composición de funciones.

    EJEMPLOS PRÁCTICOS:
    -------------------
    **) Manipulación de cadenas: Convertir una cadena a minúsculas, reemplazar 
        caracteres y dividirla en palabras.
    **) Procesamiento de datos: Filtrar, ordenar y transformar datos en una lista o 
        DataFrame.
    **) Creación de objetos: Configurar un objeto con múltiples atributos en una 
        sola línea.

    CONSIDERACIONES IMPORTANTES:
    ----------------------------
    **) Retorno del objeto: Es fundamental que cada método retorna el objeto sobre 
        el que se invoca para que el encadenamiento funcione correctamente.
    **) Orden de los métodos: El orden en el que se encadenan los métodos es crucial, 
        ya que el resultado de un método se convierte en la entrada del siguiente.
    **) Claridad: Aunque el encadenamiento de métodos puede hacer el código más 
        conciso, es importante no abusar de esta técnica, ya que un encadenamiento 
        demasiado largo puede dificultar la comprensión.

    El encadenamiento de métodos es una herramienta poderosa en Python que permite 
    escribir código más expresivo y eficiente. Al comprender cómo funciona y cuándo 
    usarlo, podrás aprovechar al máximo sus beneficios.
"""

texto = "  Hola, mundo!  "

# Primero ejecuta texto.strip()
# el resultado anterior es la entrada para .upper()
# El nuevo resultado es la nueva entreada para .split()

resultado = texto.strip().upper().split()
print(resultado)
