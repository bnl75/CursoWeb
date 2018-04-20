import random

def adivinar():
    print("Introduzca el numero que crea correcto entre el 1 y el 9")
    num = int(input("Numero: "))
    salir = False

    while (not salir):
        desc = random.randint(1,9)
        if (num == desc):
            print("Bien adivinado")
            print("Numero adivinado: " + str(desc))
            salir = True
        else:
            print("Numero incorrecto!!!")
            num = int(input("Numero: "))

adivinar()
