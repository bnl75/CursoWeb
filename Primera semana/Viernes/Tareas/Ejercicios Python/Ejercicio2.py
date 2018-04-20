# -*- coding: utf-8 -*-

def temperatura():
    print("Grados Celsius: 60°")
    print("Grados Fahrenheit: 45°")
    ctf = ((60 * 1.8) + 32)
    ftc = ((45 - 32) / 1.8)
    print("60°C = " + str(ctf) + "°F")
    print("45°F = " + str(ftc) + "°C")
    print("Fin del programa")

temperatura()
