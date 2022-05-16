# 5. El supermercado barato y algo más, presenta demoras a la hora de generar el valor total de la compra de sus clientes (se confunde el valor por producto, con la cantidad de productos, y con el valor total a cancelar, el proceso se realiza varias veces).
# Para dar solución a ese problema se sugiere una solución mediante el uso de un algoritmo. Algoritmo de una factura: que capture el valor unitario del producto, cantidad del producto.
# Se debe calcular e imprimir el valor unitario del producto, subtotal de la factura sin IVA y el valor total a pagar. Asumir el porcentaje del IVA=19%./

def total(valor, cantidad):
    subtotal = valor * cantidad
    iva = 0.19
    print('\nUnitary value: ', valor)
    print('Invoice subtotal is: ', subtotal)
    print('IVA 19% ', (subtotal * iva))
    print('Invoice total is: ', subtotal + (subtotal * iva))


menu = """
                                                  
Welcome to Supermercado barato y algo mas

choose an option

    1 - Enter  
    2 - Exit

:"""

option = int(input(menu))

if option == 1:
    value = int(input('insert the value of the products: '))
    cant = int(input('insert the quantity of the products: '))
    total(value, cant)
else:
    print('Enter a correct option ')
