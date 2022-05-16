# High order functions: filter, map y reduce

# filter the pair numbers with list comprenhentions
my_list = [1, 4, 5, 6, 7, 9, 13, 19, 21]
odd = [i for i in my_list if i % 2 != 0]
print(odd)

# Use FILTER
my_list = [1, 4, 5, 6, 7, 9, 13, 19, 21]
odd = list(filter(lambda x: x % 2 != 0, my_list))
print(odd)

#---------------------------------------------------

# Exercise Numbers elevate 2 using list comprenhentios

my_list = [1, 2, 3, 4, 5]
squares = [i**2 for i in my_list]
print(squares)

# Use MAP
my_list = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, my_list))
print(squares)

#---------------------------------------------------

# Exercise without reduce
my_list = [2, 2, 2, 2, 2]
all_multiplied = 1

for i in my_list:
    all_multiplied = all_multiplied * i

print(all_multiplied)

# Exercise with REDUCE

from functools import reduce

my_list = [2, 2, 2, 2, 2]
all_multiplied = reduce(lambda a, b: a * b, my_list)
print(all_multiplied)