def parImpar():
    print("Serie de numeros: (1, 2, 3, 4, 5, 6, 7, 8, 9)")
    serie = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    par = 0
    impar = 0

    for i in serie:
        if ((i % 2) != 0):
            impar += 1
        else:
            par += 1

    print("Numeros pares en la serie: " + str(par))
    print("Numeros impares en la serie: " + str(impar))

parImpar()
