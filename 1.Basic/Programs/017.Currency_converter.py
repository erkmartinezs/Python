def conversor(tipo_pesos, valor_dolar): 
    pesos = input('Cuantos pesos ' + tipo_pesos + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares =str(dolares)
    print('Tienes $' + dolares + ' Dolares')


menu ="""
                                                  
Bienvenido al conversor de moneda 💰

1 - pesos colombianos
2 - pesos argentinos
3 - pesos mexicanos

elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
   conversor("colombianos",3875)
elif opcion ==2:
    conversor("argeninos",65)
elif opcion == 3:
    conversor("mexicanos",24)
else: 
    print('ingresa una opcion correcta: ')