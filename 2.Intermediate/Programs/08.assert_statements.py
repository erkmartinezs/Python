def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():

    num = input('Enter the number: ')
    assert num.isnumeric(), 'You must enter a number'
    print(divisors(int(num)))
    print('Finish Program')


if __name__ == '__main__':
    run()