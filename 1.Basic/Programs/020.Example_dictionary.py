from select import POLLRDBAND


def run():
    Mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(Mi_diccionario['llave1'])
    # print(Mi_diccionario['llave2'])
    # print(Mi_diccionario['llave3'])
    print(Mi_diccionario)

    poblacion_paises = {
    'Argentina': 44938712,
    'Brasil': 210147125,
    'Colombia': 5037242
    }
    print(poblacion_paises)

    for pais in poblacion_paises.keys():
        print(pais) 

    for pais in poblacion_paises.values():
        print(pais) 
 
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')    

if __name__ == '__main__':
    run()