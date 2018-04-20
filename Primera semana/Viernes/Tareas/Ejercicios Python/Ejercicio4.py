def figura():
    car1 = "*"
    car2 = ">"
    repetir = 0

    for i in [0,1,2,3,4,5]:
        repetir += 1
        print(car1 * repetir)
        print(car2 * repetir)
    print(car1 * (repetir + 1))
    for i in [0,1,2,3,4,5]:
        repetir -= 1
        print(car2 * repetir)
        print(car1 * repetir)

figura()
