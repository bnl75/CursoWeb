def salto():
    serie = [0, 1, 2, 3, 4, 5, 6]
    print("serie = [0, 1, 2, 3, 4, 5, 6]")

    for i in range(0,len(serie)):
        if ((serie[i] == 3) or serie[i] == 6):
            continue

        print("Resultado: " + str(serie[i]))


salto()
