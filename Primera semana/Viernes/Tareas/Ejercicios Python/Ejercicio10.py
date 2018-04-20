def vocales():
    cadena = list(input("Ingrese una cadena de texto: "))

    for i in cadena:
        if ((i == 'a') or (i == 'e') or (i == 'i') or (i == 'o') or (i == 'u') or (i == 'A') or (i == 'E') or (i == 'I') or (i == 'O') or (i == 'U')):
            continue
        print(i)


vocales()
