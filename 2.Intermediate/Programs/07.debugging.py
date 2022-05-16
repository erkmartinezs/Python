def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors
    print('Finish Program')


def run():

    try:
        num = int(input('Enter the number: '))
        if num < 0:
            raise ValueError('Enter a correct number')
        return print(divisors(num))

    except ValueError:
        print('Enter a correct number')
        return False


if __name__ == '__main__':
    run()