# Actividad
# Condiciones:
# • El subcidio de trasporte lo reciben empleados que ganen hasta dos salarios mínimos legales  vigentes,averiguar valor del SMLV.
# • El valor de una hora extra tiene un incremento del 30% sobre el valor de una hora normal
# • Las comisiones por ventas tienen un valor del 20% sobre las ventas realizadas en el mes.

# Como resultado del ejercicio se debe imprimir en pantalla lo siguiente:
# Cedula empleados: XXXXXX
# Nombres y Apellidos Empleado: XXXXXXX
# Salario Básico: XXXXXX
# Auxilio de Transporte: XXXXXX
# Comisión de Ventas: XXXXXX
# Préstamos: XXXXXX
# Salario Neto a Recibir: XXXXX
# Calcular e imprimir el promedio de los salarios básicos de los empleados
# Hallar el menor y el mayor salario neto e identificar a que empleado corresponde.
# Se debe utiliza un método para leer los datos de entrada ,otro para calcular las comisiones por
# ventas y otro para imprimir los datos de salida.
# El algoritmo debe contener:
# • Diseño y codificación de algoritmos utilizando diferentes tipos de métodos funciones o
# subprocesos.

smlv = 908526
aux = 117172


def auxTransporte(valor):
    if valor <= (smlv * 2):
        print('Auxilio de Transporte: $ ' + str(aux))
    else:
        print('Auxilio de Transporte: $ 0')


def comisionVentas(valor):
    comision = valor * 0.20
    print('Comisión de Ventas: $ ' + str(comision))


def prestamos():
    pass


def salarioNeto():
    pass


n = int(input('Enter the number of employees to settle monthly payroll: \n'))

if n > 0:
    for i in range(0, n):
        print('///////////////////////////////////////////')
        cedula = input('Ingrese numero de cedula: ')
        nombres = input('Ingrese Nombres del Empleado: ')
        apellidos = input('Ingrese Apellidos del Empleado: ')
        salario = int(input('Ingrese el Salario Básico: '))
        ventas = int(input('Ingrese el valor de comisiones por Ventas: '))
        print('*******************************************')

        if i < n:

            print('Resume: ')
            print('\n' + 'Cedula empleado: ' + cedula)
            print('Nombres y Apellidos Empleado: ' + nombres + ' ' + apellidos)
            print('Salario Básico: $' + str(salario))
            auxTransporte(salario)
            comisionVentas(ventas)
            # print('Préstamos: ' + cedula)

else:
    print("The number entered is not correct. Try again.")
