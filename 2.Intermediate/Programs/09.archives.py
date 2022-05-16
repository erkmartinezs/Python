def read():
    numbers = []
    with open('./archives/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ['Erik', 'Quentin', 'Fernanda', 'Alexander', 'Rocio']
    with open('./archives/names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def append():
    names = ['Maria', 'Luis', 'Miguel', 'Nicolas', 'Daniel']
    with open('./archives/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    append()


if __name__ == '__main__':
    run()