import math
from functools import reduce

# for x in range(1, 31, 5):
#     print(x)
#
#

# numbers = [1, 2, [1, 2]]
# print(numbers[::-1][1:3])
#
# numbers_new = numbers.copy()
# print(id(numbers[2]), id(numbers_new[2]))
# numbers_new[2].pop(1)
# numbers_new[2][0] = 5
# print(numbers, id(numbers))
# print(numbers_new, id(numbers_new))

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = [elem for row in matrix for elem in row]
# print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# result = []
# for elem in matrix:
#     result.extend(elem)
# print(result)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# enumerate_numbers = enumerate(numbers)
# print(type(list(enumerate_numbers)[0]))

# tup = (1, 2, 3)
# a, b, c = tup
# print(a, b, c)
# a = 12
# print(tup)
# print(a, b, c)

# a, b, c = 'hel'
# print(a, b, c)

# a = 'hell',
# print(a)

# divisible_by_2 = [x for x in range(1, 10) if x % 2 == 0]
# divisible_by_3 = [x for x in range(1, 10, 2) if x % 3 == 0]
# non_divisible_by_and_3 = [x for x in range(1, 10) if not x % 2 == 0 and not x % 3 == 0]
# print(divisible_by_2)
# print(divisible_by_3)
# print(non_divisible_by_and_3)

# def print_test(*args):
#     print(*args, type(args))
#     print(args, type(args))
#
#
# print_test("hello", "world")

# def arithmetic_mean(*numbers):
#     return sum(numbers) / len(numbers)
#
#
# print(arithmetic_mean(1, 2, 3, 4, 5, 353, 123, 123145, 2, 2,))

# def cal_factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * cal_factorial(n - 1)
#
#
# print(cal_factorial(5))


# def number_of_characters(string: str):
#     result = {}
#     for index, character in enumerate(string):
#         if character in result:
#             result[character] += 1
#             continue
#         result[character] = 1
#     return result
#
#
# print(number_of_characters('asldkgfjskdjlfjvdiusj'))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(str, numbers)))
# print(list(map(lambda x: x * 2, numbers)))

# def replace_chr(string: str, old: str, new: str):
#     result_string = ''
#     for letter in string:
#         if letter == old:
#             letter = new
#         result_string += letter
#     return result_string
#
#
# print(replace_chr('rEplace', 'e', 'A'))
#
#
# def replace_chr1(string: str, old: str, new: str):
#     return ''.join(map(lambda letter: new if letter == old else letter, string))
#
#
# print(replace_chr1('rEplace', 'e', 'A'))

# class Encapsulation(object):
#     def __init__(self, a, b, c):
#         self.public = a
#         self._protected = b
#         self.__private = c
#
# x = Encapsulation(11,13,17)
# print(x._protected)
# x._protected = 23
# print(x.__private)

# class P:
#     def __init__(self, x):
#         self.x = x
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x

# class P:
#     def __init__(self, x):
#         # self.__set_x(x)
#         self.__x = x
#
#     def __get_x(self):
#         return self.__x
#
#     def __set_x(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
#
#     def __repr__(self):
#         return f"{self.__x}"
#
#     x = property(__get_x, __set_x)
#
#
# p = P(5)
# p.x = 1
# print(p.x)
#
# class CustomError(Exception):
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return repr(self.data)

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Что-то делаем до вызова функции")
#         func(*args, **kwargs)
#         print("Что-то делаем после вызова функции")
#     return wrapper
#
#
# @my_decorator
# def say_hello(name):
#     print(f"Привет, {name}!")
#
#
# # Использование декорированной функции
# say_hello("Alice")

# names = ['Sam', 'Don', 'Daniel']
# for i in range(len(names)):
#     names[i] = hash(names[i])

# names = list(map(lambda x: hash(x), names))
# print(names)

# strings = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
# strings = list(filter(lambda x: x == 'red', strings))
# print(strings)

# numbers = ['1', '2', '3', '4', '13', '5', '7']
# numbers = list(map(int, numbers))
# numbers_result = []
# for number in numbers:
#     numbers_result.append(int(number))
# print(numbers_result)

# biggest = reduce(lambda x, y: x if x > y else y, numbers)
# print(biggest)

# string = 'hollahhlasdfgh'
# string = ''.join(list(map(lambda x: x.replace(x, 'e') if x == 'h' else x, string)))
# print(string)

# def range_analog(start: int = 0, stop: int = 1, step: int = 1):
#     while start < stop:
#         yield start
#         start += step
#
#
# print(list(range_analog(start=1, stop=10, step=2)))

# def make_pretty(func):
#     def wrapper(*args, **kwargs):
#         print('*' * 30)
#         func(*args, **kwargs)
#         print('*' * 30)
#
#     return wrapper
#
#
# @make_pretty
# def test(te):
#     print(f'do {te}')
#
#
# test('tuta')

# with open('test.txt', 'a', encoding='utf8') as file:
#     file.write('\nHello World')

# import json
#
# json_string = """
# {
#     "firstName": "Ivan", "lastName": "King",
#     "hobbies": ["reading", "traveling", "singing"],
#     "age": 33,
#     "children":
#         [
#             {
#                 "firstName": "Vira",
#                 "age":
#                     3
#             }, {
#             "firstName": "Maksym",
#             "age":
#                 5
#         }
#         ]
# }
# """
# json_d = json.loads(json_string)
# print(json_d, type(json_d), type(json_string))
# resu = json.dumps(json_d)
# print(resu, type(resu))