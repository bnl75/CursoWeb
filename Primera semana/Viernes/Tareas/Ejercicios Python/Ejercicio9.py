def factorial(x):
    if (x > 1):
        return x * factorial(x - 1)
    else:
        return 1

num = int(input("Factorial del numero: "))
print("Resultado: " + str(factorial(num)))
