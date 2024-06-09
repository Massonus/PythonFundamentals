





list_colors = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"] 

def ff1(x):
    return x == "red"


new_1 = list(map(ff1, list_colors))
print(new_1)

new_2 = list(filter(lambda x: x == "red", list_colors))
print(new_2)


#map
# name_lengths = map(hash, ['Dick', 'Nick', 'Leonardo'])
# print(list(name_lengths))

# name_lengths = map(int, ['17', '89', '7'])
# print(list(name_lengths))
# or
# for lengths_obj in name_lengths:
#     print(lengths_obj)
############################3
# list_1 = [0, 1, 2, 3, 4]
# squares = map(lambda x: x**2, list_1)
# print(squares)

####################################################

####################3
#  map, є випадки коли 
# необхідно застосувати
# функцію до кожного 
# елемента списку 
######################
#реалізація без 
# використання map 
##################
# def f(x):
#     return x*x

# nums = [1, 2, 3]
# for num in nums:
#     print(f(num))
######################
#реалізація з використанням
#list comprehensions
##################
# nums = [1, 2, 3]

# def f(x):
#     return x*x

# g=[f(num) for num in nums]
# for item in g:
#     print(item)


# реалізація з 
# використанням map
#################

# nums = [1, 2, 3]
# def f(x):
#     return x*x
# g=map(f, nums)
# for item in g:
#     print(item)

################
#реалізація з допомогою
#map і lambda
################
# nums = [1, 2, 3]

# g=map(lambda x: x*x, nums)

# print(g)

# for item in g:
#      print(item)


#################
#map застосовує деяку 
#функцію до списку і повертає
# результат знову у вигляді
#списку. 
######################## 
# Ми можемо передати декілька
# списків, тоді функція,
# яка йде першим параметром
# повинна приймати декілька
# аргументів (по 
# кількості списків переданих
#  в map).
#####################
# def f(x, y):    
#     return x*y

# a = [1,3,4]
# b = [3,4,5]

# g=map(f, a, b)

# for item in g:
#     print(item)
# #######################

#######################
#якщо списки різної довжини,
#то необхідно робити перевірку
#на None(Python version 2) 
#####################
# def f(x, y):    
#     if (y == None):
#         y = 1
#     if (x == None):
#         x = 1
#     return x*y

# a = [1,3,8,4,7]
# b = [3,4,9]
# g=map(f, a, b)
# print(list(g))
# #####################
# #(Python version 2) 
# # А тепер добре б 
#передати списки 
#відсортовані по 
#довжині – 
#len(a) > (b) – просто
#скористаємось функцією
#sorted :
#фунция sorted 
# приймає список
# значень 
#([a,b] = [[1,2],[2,4,5]]) 
#і сортуємо по ключу 
# key – який в нас 
# заданий функцією len(x),
# яка повертає довжину
# списку, сортуємо в порядку
# спадання (reverse=True)
#списки a і b можуть бути
# різної довжини і передаватися 
# в будь-якому порядку.
#########################
# a = [1,3,4]
# b = [3,4]
# g=map(lambda x, y: x * (y if y is not None else 1), 
# *sorted([a, b], key=lambda x: len(x), reverse=True))
# print(list(g))
##################


# names = ['Sam', 'Don', 'Daniel'] 


# # for i in range(len(names)): 
# #     names[i] = hash(names[i]) 

# hash_names = map(hash , names)

# print(list(hash_names)) 






