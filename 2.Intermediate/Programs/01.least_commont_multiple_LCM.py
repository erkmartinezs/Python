def run():
    x = int(input('enter the first number: '))
    y = int(input('enter the second number: '))
    w = int(input('enter the third number: '))

    def mcm(x, y, w):

        z = max(x, y, w)
        while True:
            if (z % x == 0) and (z % y == 0) and (z % w == 0):
                return z
            z += 1
    print('The least common multiple of: ' +
          str(x) + ', ' + str(y)+', ' + str(w))
    print(mcm(x, y, w))


if __name__ == '__main__':
    run()
