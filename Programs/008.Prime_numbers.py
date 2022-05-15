n = int(input('Up to what number do you want the list of prime numbers?: '))

if n > 0:
    for i in range(2, n + 1):
        creciente = 2
        esPrimo = True
        while esPrimo and creciente < i:
            if i % creciente == 0:
                esPrimo = False
            else:
                creciente += 1
        if esPrimo:
            print(i, "is prime.")
else:
    print("The number entered is not correct. Try again.")
