# Numbers in range 1-100 calculate cubed value
def run():
    my_dict = {}

    for i in range(1, 101):
        my_dict[i] = i**3

    print(my_dict)


if __name__ == '__main__':
    run()

#--------------------------------------------------------


# Calculate cubed number to numbers not divisible in 3
def run():
    my_dict = {}

    for i in range(1, 101):
        if i % 3 != 0:
            my_dict[i] = i**3

    print(my_dict)


if __name__ == '__main__':
    run()

#--------------------------------------------------------

# Dictionary Comprehentions


def run():
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print(my_dict)


if __name__ == '__main__':
    run()

# Dictionary Comprehentions exercise squarred root

from math import sqrt


def run():
    my_dict = {i: sqrt(i) for i in range(1, 1001)}

    print(my_dict)


if __name__ == '__main__':
    run()
