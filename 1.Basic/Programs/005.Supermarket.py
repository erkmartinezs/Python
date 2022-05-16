# 1. Don Pablo Mármol en su supermercado tiene una oferta vigente por compras superiores o iguales de $178.000 aplicando un descuento de 11%. Si la compra corresponde a un valor menor aplica un descuento del 2%. Calcular e imprimir el valor de la compra, valor del descuento y el valor total de la compra aplicando el descuento.


def discount(valor):
    if valor >= 178000:
        print('Purchase value: $' + str(valor))
        print('Purchase discount: 11%')
        print('Total to pay: $' + str(valor - (valor * 0.11)))
    else:
        print('Purchase value: $' + str(valor))
        print('Purchase discount: 2%')
        print('Total to pay: $' + str(valor - (valor * 0.02)))


menu = """
                                                  
Welcome to the shopping calculator

Enter the value of the purchase:

"""

compra = int(input(menu))

if compra >= 0:
    discount(compra)
else:
    print('Enter a correct option ')
