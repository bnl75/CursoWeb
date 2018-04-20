def encontrarNumero():
    num = 1499
    while (num < 2701):
        num += 1
        if ((num % 5) == 0 and (num % 7) == 0):
            print("Numero divisible entre 7 y multiplo de 5: " + str(num))

    print("No hay mas numeros!!!")

encontrarNumero()
