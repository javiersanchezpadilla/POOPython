""" MULTIPLES CONTEXT MANAGER

    ¿Puedo mezclar diferentes modos de apertura?
    --------------------------------------------
    Sí Cada archivo puede tener su propio modo:

    En Python 3.10 y versiones posteriores, también puedes usar paréntesis 
    para múltiples líneas:

            with (
                open("archivo1.txt", "r") as f1,
                open("archivo2.txt", "r") as f2,
                open("archivo3.txt", "w") as f3
            ):
                f3.write(f1.read() + f2.read())
"""
with open("datos.txt", "r") as lectura, \
     open("escritura.txt", "w") as escritura, \
     open("log.txt", "a") as log:
    
    datos = lectura.read()
    escritura.write(datos.upper())
    log.write("Copia realizada\n")
    # Los tres se cierran juntos
