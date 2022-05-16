def primos(x, y):
    for i in range(x, y + 1):
        creciente = 2
        esPrimo = True
        while esPrimo and creciente < i:
            if i % creciente == 0:
                esPrimo = False
            else:
                creciente += 1
        if esPrimo:
            print(i, "is prime.")


start = int(
    input('At what number do you want to start the validation of prime numbers?: '))
end = int(
    input('In what number do you want to finish the validation of prime numbers?: '))

if start < end:
    primos(start, end)
else:
    print("The number entered is not correct. Try again.")
