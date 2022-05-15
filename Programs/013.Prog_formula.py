def serie(n):
    for i in range(1, n):
        print((i*(i+1)) ^ 2)


num = int(input('enter the number up to which you want to calculate: '))

serie(num)
