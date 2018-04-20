def tipo():
    datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"clase": 'V', 'section': 'A'} ]

    print("Elementos en datalist")
    for i in range(0,len(datalist)):
        print(str(datalist[i]) + ": " + str(type(datalist[i])))

tipo()
