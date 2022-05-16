def run():
    my_list = [1, 'Hello, True, 4.5']
    my_dict = {'firstname': 'Erik', 'lastname': 'Martinez'}

    super_list = [
        {'firstname': 'Erik', 'lastname': 'Martinez'},
        {'firstname': 'Pepito', 'lastname': 'Perez'},
        {'firstname': 'Esperanza', 'lastname': 'Gomez'},
        {'firstname': 'Quentin', 'lastname': 'Martinez'}
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }

    # ciclo for super_dict
    for key, value in super_dict.items():
        print(key, '-', value)

    # ciclo for super_list
    for item in super_list:
        print(item["firstname"], "-", item["lastname"])


if __name__ == '__main__':
    run()
