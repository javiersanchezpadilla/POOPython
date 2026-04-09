""" USO DE __name__

    Suponer que mi programa B11_Imports01.py contiene

        variable = "Variable de mi modulo"

        def mi_funcion():
            print("Hola desde mi funcion")

        class MiClase:
            def __init__(self):
                print("Hola desde mi clase")


        if __name__ == '__main__':
            print(variable)
            mi_funcion()
            a = MiClase()

        print('Como modulo no queremos esta impresión') <<<<<<<<<<<<<<<<<<<

    Al momento de ejecutar el programa como módulo imprimiria siempre esta 
    linea, para corregirlo incluirlo dentro de if __name__
    
        if __name__ == '__main__':
        print('Como módulo no queremos esta impresión')

"""