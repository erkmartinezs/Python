def datos(nombre, apellido, edad):
    print('Full name: ' + nombre + ' ' + apellido)
    print('Age: ' + edad + ' Years old')


name = input('please, enter your name: ')
lastName = input('please, enter your last name: ')
age = input('please, enter your age: ')
print('\n')
print(datos(name, lastName, age))
