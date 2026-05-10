""" TRACEBACK   

    Error común: Confundir la causa con el efecto


"""
def pedir_edad():
    edad = int(input("Edad: "))  # Si el usuario escribe "veinte", ValueError 
                                 # aquí
    return 100 / edad            # Si edad es 0, ZeroDivisionError aquí
