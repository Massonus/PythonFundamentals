vec1 = [3, 10, 2, 67]
vec2 = [-20, "5", 1, True, 78, 5, 3]


# # # vec3 = [1, 2, 3, 7, 78]


# print(zip(vec1, vec2))
# print(type(zip(vec1, vec2)))
# print(list(zip(vec1, vec2)))

# for item in zip(vec1,vec2):
#     print("zip",item)


# # # print(list(zip(vec1, vec2)))

# print(list(zip(vec1, vec2, vec3)))

# for item in zip(vec1,vec2, vec3):
#     print(item)

# vec1 = [3, 10, 2, 67, 78, 89]
# vec2 = [-20, 5, 1, 89]

# dot_mul = [u*v for u, v in zip(vec1, vec2)]


# print(dot_mul)

# print(sum(dot_mul))
# print(list(zip(vec1, vec2, vec3)))



# for item in zip(vec1,vec2,vec3):
#     print(item)

# print(dot_mul)


#zip це аналог застібки,
#функція бере на вхід 
# декілька списків і 
# створює з них список
# (в Python 3 створюється
# не list, а спеціальний 
# zip-обєкт) кортежів, 
#такий, що перший елемент 
# отриманого списку містить
# кортеж з перших елементів 
#всіх списків-аргументів. 
#######################
# a = [1,2]
# b = [3,4]
# g=zip(a,b)
# print(g)
# for item in g:
#     print(item)
# ###############
# a = [1,2]

# b = [3,4]

# c = [5,6]
# g=zip(a,b,c)
# for item in g:
#     print(item)
####################
###################
#  * перед list говорить
# що передається список 
# аргументів
###############

# a = [1,2]
# b = [3,4]
# c = [5,6]
# list1 = [a, b, c]
# print(list1)




# g1=zip(list1)
# print("without*:", list(g1))
# # # # # # #####################
# g=zip(*list1)
# print("from*:", list(g))


# # for item in g1:
#      print(item)
# # ######################
# # в сукупності з оператором * 
# # функція zip може бути 
# # використана для розпаковки 
# # списку:
# ############
# first, second = zip(*[(1, 4), (2, 5), (3, 6)])  

# print(first)
# print(second)

####################
# a = [10, 20, 30, 40]
# b = ['a', 'b', 'c', 'd', 'e']

# for i, j in zip(a, b):
#     print(i, j)

# print(zip(a,b))
# print(list(zip(a,b)))
# print(dict(zip(a,b)))

# #################3
# a = [10, 20, 30, 40]
# b = ['a', 'b', 'c', 'd', 'e']

# for i in zip(a, b):
#     print(i, type(i))
# print(type(zip(a,b)))
########################

# from itertools import zip_longest

# a = [10, 20, 30, 40]
# b = ['a', 'b', 'c', 'd', 'e']
# c = [1.1, 1.2]

# for i in zip_longest(a,b,c):
#     print(i)

# ###############################
# a = [10, 20, 30, 40]
# b = ['a', 'b', 'c', 'd', 'e']
# c = [1.1, 1.2]
# for i in zip(a,b,c):
#     print(i)

# for i in itertools.zip_longest(a,b,c):
#     print(i)
#####################3
# import random
# names = ['Sam', 'Don', 'Sid'] 
# code_names = ['Iron', 'Batman', 'Capitan'] 
# for i in range(len(names)): 
#     names[i] = random.choice(code_names) 
# print(names)





