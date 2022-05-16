def run():
    #code extract to commments in platzi (ret)
    squares = [i for i in range(1, 100000) if i % 36 == 0]
    print(squares)

    # code without list comprenhensions
    squares = []
    for i in range(1, 101):
        # print(i)
        if i % 3 != 0:
            squares.append(i**2)
    print(squares)

    # code with list comprenhensions
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)


if __name__ == '__main__':
    run()
