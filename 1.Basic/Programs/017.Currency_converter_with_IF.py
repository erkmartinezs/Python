menu ="""
Bienvenido al conversor de moneda 💰´ 

1 - pesos colombianos
2 - pesos argentinos
3 - pesos mexicanos

elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input('Cuantos pesos colombianos tienes?: ')
    pesos = float(pesos)
    valor_dolar =3875
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares =str(dolares)
    print('Tienes $' + dolares + ' Dolares')
elif opcion ==2:
    pesos = input('Cuantos pesos argentinos tienes?: ')
    pesos = float(pesos)
    valor_dolar =65
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares =str(dolares)
    print('Tienes $' + dolares + ' Dolares')
elif opcion == 3:
    pesos = input('Cuantos pesos mexicanos tienes?: ')
    pesos = float(pesos)
    valor_dolar =24
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares =str(dolares)
    print('Tienes $' + dolares + ' Dolares')
else: 
    print('ingresa una opcion correcta: ')


