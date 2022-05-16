#######---------1.Consepts basics in python ---------------------

x = 1
y = x+1
z = "Hello World"
print(x ,y, z, "bitches" )

#######---------2. Libraries - import libraries ---------------------

# import by library name
from doctest import Example
import random
x = random.randint(1,6)
print(x)

# import especific funtion
from random import randint
randint(1,6)

#import all from library
from random import *
print(randint(1,6))


#######----------3. request data from the user---------------------

x = input("Enter a numeric value ")
print(x)


#######---------4.Condicionales---------------------------------------
# logic operators >, <, >=, <=, ==, !=

x = 5
y = 4

print(x < y)
print(x > y)
print(x == y)
print(x != y)
print(True and False)
print(True or False)

print( x >=5 and y == 4)


#ejemplo

import random

x = random.randint(1, 5)

if x== 1:
    print("Numero 1")
elif x == 2:
    print("Numero 2")
elif x == 3:
    print("Numero 3")
else:
    print("Other Number")
print(x)



#######---------5.loops for and while ----------------
import random
x = 0
for i in range(10):
    print(i)
    x += random.randint(1, 5)

x = 0
while x !=5:
    x = random.randint(1, 100)

    print(x)

#######---------6.lists --------------------
numeros = [9, 2, 3, 8, 5, 6, 7]

print(numeros[3])
print(numeros[-1])

numeros.append(10) ## agrega al final
numeros.remove(6) ## remueve el numero
numeros.pop(0) ## remueve el indice 

numeros[0] = 500 ## reemplaza numero por su indice

print(len(numeros)) ## muestra longitud de la lista
print(numeros.index(8)) ## muestra numero en indice 
print(6 in numeros) ## show true or false if 6 is in the list
numeros.sort() ## show numbers upward
numeros.reverse() ## show numbers downward
print(numeros)

for elem in numeros:
print(elem)

for i in range(len(numeros)):
    print(numeros[i])


#######---------7.text strings ----------------

cadena = "Hello World"

print(len(cadena)) ## shows the length of the string
print( cadena[2] ) ## returns index 2 in string

for c in cadena:  ## returns the index of a string
    print(c)

print(cadena.lower()) ## return string in lowercase
print(cadena.upper()) ## return string in uppercase
print(cadena.capitalize()) ##return first letter in uppercase
print(cadena.startswith("hello")) ## returns true or false if string start with "xxxx"
print(cadena.endswith("hello")) ## returns true or false if string ends with "xxxx"
print(cadena.startswith("hello")) ## returns true or false if string start with "xxxx"
print(cadena.isalpha()) ## returns true or false if is string
print(cadena.isdigit()) ## returns true or false if is numbers
print(cadena.isalnum()) ## returns true or false if is alphanumeric
print(cadena.islower()) ## returns true or false if all characters are lowercase
print(cadena.isupper()) ## returns true or false if all characters are uppercase
print(cadena.strip()) ## returns string without spaces

fruits = "apple, pear, blueberry"
print(fruits.split(",")) ## separate strings with character ","

lista = fruits.split(",")
string_2 = "-".join(lista) ## join strings with character "-"
print(string_2)


#######---------7.Tuplas----------
##Listas inmutables use ()

var = (1, 5, 9)
print(var)

var2 = [2, 3, 8]
tupla = tuple(var2) ## change list to tuple
print(type(var2)) # print type -- list
print(type(tupla)) # print type -- tuple


#######---------9.Conjuntos-----------
##No mantienen un order (no son structuras indexables) 
# no guardan elementos repetidos

lista = [1, 5, 6] ## create list -- with []
conjunto =  set(lista) ## change list to set
print(type(lista))
print(type(conjunto))

conjunto2 = {3, 7, 4} ## create Set --with {}
print(conjunto2)

conjunto2.add(10) ## aggregate 10 to set, not aggregate duplicate
conjunto2.remove(10) ## remove 10 to set


conjunto2 = {3, 7, 4}
for elem in conjunto2:  ## list the elements in set
    print(elem)

print ( 5 in conjunto2) ## valid if 5 is in the set

conj1 = {1, 5, 9}
conj2 = {2, 5, 8}
print(conj1.union(conj2)) ## union sets
print(conj1.intersection(conj2)) ## intersection sets


#######---------10. Dictionaries -------------------
## laLos diccionarios son pares, se puede comparar con Mongo o formato json
# Clave-valor
# Acceder a los valores a través de las claves (Comparacion con indices)

dictionary = {   ##create dictionary key-value
    "Name": "Erik",
    "age": 25,
    "rol": "BI Analyst Sr"
}
dictionary["last_name"] = "Martinez" ## we add key last_name to dictionary
print(dictionary)  ## we show all information in the dictionary
print(dictionary["age"]) ## print key age in the dictionary

dictionary["example"] = "eliminate" "" ##create key example for to eliminate
del dictionary["example"] ## eliminate example
dictionary["age"] = 20 ## change key age to 20
dictionary["age"] += 5 ## add +5 to existing age 

dictionary

for k, v in list(dictionary.items()):   ## run the dictionary changing to list
    print(k,v)

dict2 = {   ##create dictionary key-value
    "Name": ["Hello World", 20],
    "age": {"age_2": 25,
            "name_2": "Alexander"}
} ## 

print(dict2["age"]["age_2"])


#######---------11. Funciones -------------------
## def define nombre funcion y en () se ingresan parametros 
def suma(lista):
    x = 0
    for elem in lista:
        x += elem 
    return x

sumatoria = suma([1,2,3,4,5])
print(sumatoria)

#######---------12. archivos -------------------
## modos de apertura  R-Read A-append W-Write

f = open("frutas.txt", "a")
f.write("mango,10,10\n")


#######---------13. Errores y Exepciones -------------------
## nos ayuda a realizar debugging and skip code in case of error
cadena = "hola"
try:    
    x = int(cadena)  ## volatile code to errors 
except Exception as err:
    print("Errorrr!") ## code in case of error

print("Final!")


#######---------14. clases POO -------------------
## programacion orientada a objetos *no es claro el video, estudiar mas*

class Persona:

    especie = 'Humano'

    def __init__(self, edad, pais):
        self.edad = edad
        self.pais = pais

    def dormir(self):
        print("zzzz")

    def cumpleanio(self):
            self.edad += 1

persona = Persona(50, "Islandia")
persona.dormir()
print(persona.edad)

class Programador(Persona):
    def __init__(selft, edad, pais, experiencia):
        Persona.__init__(selft, edad, pais)
        selft.anios_experiencia = experiencia

    def dormir(self):
        print("not found")

yo = Programador(25, "Colombia", 7)
yo.dormir()
yo.cumpleanio()
print(yo.edad)
    