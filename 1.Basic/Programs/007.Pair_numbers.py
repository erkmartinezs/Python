n = int(input('Enter a limit number: '))

if n > 0:
    for i in range(0, n+1, 1):
        if i % 2 == 0:
            print(i, ' Is a even number and its square is: ', i ** 2)
else:
    print("The number entered is not correct. Try again.")
