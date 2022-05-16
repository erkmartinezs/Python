def cuadrado():
    lado_c = input('Cuanto mide en centimetros un lado del cuadrado?: ')
    lado_c = int(lado_c)
    area_c = lado_c ** 2
    perimetro_c = lado_c * 4
    print('El area del cuadrado es:' + str(area_c) + ' centimetros')
    print('El perimetro del cuadrado es:' + str(perimetro_c) + ' centimetros')


def rectangulo():
    lado_r_a = input(
        'Cuanto mide la parte izquierda o derecha del rectangulo?: ')
    lado_r_b = input(
        'Cuanto mide la parte superior o inferor del rectangulo?: ')
    area_r = int(lado_r_a) * int(lado_r_b)
    perimetro_r = 2 * (int(lado_r_a) + int(lado_r_b))
    print('El area del rectangulo es:' + str(area_r) + ' centimetros')
    print('El perimetro del rectangulo es:' +
          str(perimetro_r) + ' centimetros')


def circulo():
    radio = input('Cuanto mide el radio del circulo?: ')
    area_ci = 3.1415926535 * int(radio) ** 2
    perimetro_ci = 2 * 3.1415926535 * int(radio)
    print('El area del circulo es:' + str(area_ci) + ' cm2')
    print('El perimetro del circulo es:' + str(perimetro_ci) + ' cm2')


menu = """
                                                  
Bienvenido a la calculadora de figuras geometricas

Escoge la figura a calcular Area y Perimetro

1 - Cuadrado
2 - Rectangulo
3 - Circulo

elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    cuadrado()
elif opcion == 2:
    rectangulo()
elif opcion == 3:
    circulo()
else:
    print('ingresa una opcion correcta: ')
