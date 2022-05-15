def tabla(n):
    print('Tabla de multiplicar del numero: ' + str(n) + '\n')
    for i in range(1, 11):
        print(str(n)+' x ' + str(i) + ' =  ' + str(n * i))


num = int(input(
    'enter the number to calculate the multiplication table up to the number 10: '))

tabla(num)
