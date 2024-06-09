#функція reduce 
# приймає 2 аргумента:
# функцію і послідовність. 
# reduce() послідовно
# застосовує функцію-аргумент
# до елементів списку,
# повертає одне значення. 
# В Python 2.x функція reduce
# доступна як вбудована, 
# в Python 3 вона переміщена 
# в модуль functools.

# from functools import reduce

# items = [1,2,3,4,5]
# sum_all = reduce(lambda x,y: x + y, items)
# print(sum_all)

##########################
# from functools import reduce

# def a_add_b(a, b):
#     print("a:{} b:{}".format(a, b))
#     return a+b

# print(reduce(a_add_b, [47,11,42,13])) 
############################
# from functools import reduce

# sentences = ['capitan America', 
#              'capitan Jak',
#              'capitan']

# cap_count = reduce(lambda a, x: a + x.count('capitan'),
#                    sentences,
#                    0)

# print(cap_count)