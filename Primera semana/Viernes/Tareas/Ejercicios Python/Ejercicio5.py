def inventir():
    palabra = input("Ingrese una palabra: ")
    invertida = ""

    for i in palabra:
        invertida = i + invertida

    print("Palabra invertida: " + invertida)

inventir()
