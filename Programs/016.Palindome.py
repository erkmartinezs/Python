# def palindromo(palabra):
#     palabra = palabra.replace(' ','')
#     palabra = palabra.lower()
#     palabra_invertida = palabra[::-1]
#     if palabra == palabra_invertida:
#         return True
#     else:
#         return False

# def run():
#     palabra = input('Escribe una palabra: ')
#     es_palindromo = palindromo(palabra)
#     if es_palindromo == True:
#         print('Es palindromo')
#     else:
#         print('No es palindromo ')


# if __name__ =='__main__':
#     run()


def es_palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    
    if palabra[::] == palabra[::-1]:
        return True
    
    else:
        return False


def run():
    palabra = input('Ingrese una palabra: ')
    if es_palindromo(palabra):
        print('Es palindromo')

    else:
        print('No es palindromo')


if __name__ == "__main__":
    run()

    