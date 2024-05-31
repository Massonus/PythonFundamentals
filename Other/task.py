# first_number = float(input("Enter first number: "))
# second = float(input("Enter second number: "))
#
# if first > second:
#     print(f"The {first} number is greater than the {second} number")
# elif first < second:
#     print(f"The {second} number is greater than the {first} number")
# else:
#     print(f"{first} and {second} numbers are equal")


# if first_number % 2 == 0:
#     print(f"{first_number} is an even number.")
# else:
#     print(f"{first_number} is not an odd number.")


# print(f"{first_number} is an even number" if first_number % 2 == 0 else f"{first_number} is not an even number.")

# i = 1
# while i < 100:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1

# for i in range(100):
#     if i % 2 == 0:
#         print(i, end=" ")

# def count_digits(number):
#     if type(number) is str or type(number) is float:
#         return "Wrong data type"
#
#     return len(list(str(abs(number))))
#
#
# print(count_digits(1.5))

# def gradeCalculator(grade):
#     if 0 < grade < 50:
#         print("F")
#     elif 50 < grade < 60:
#         print("E")
#     elif 60 < grade < 70:
#         print("D")
#     elif 70 < grade < 80:
#         print("C")
#     elif 80 < grade < 90:
#         print("B")
#     elif 90 < grade < 100:
#         print("A")
#     else:
#         print("Wrong number")

# def sortNumbers(num1, num2, num3):
#     if num1 > num2:
#         num2, num1 = num1, num2
#
#     if num2 > num3:
#         num3, num2 = num2, num3
#
#     if num1 > num2:
#         num2, num1 = num1, num2
#
#     print(num1, num2, num3)
#
#
# sortNumbers(10, 20, 50)

# def calculator(number1, number2, operator):
#     if operator == '+':
#         print(number1 + number2)
#     elif operator == '-':
#         print(number1 - number2)
#     elif operator == '*':
#         print(number1 * number2)
#     elif operator == '/':
#         print(number1 / number2)
#     else:
#         print("Wrong operator")

# def is_isogram(word):
#     for letter in word:
#         if letter == "i" or letter == "I":
#             return True
#         elif letter == "s" or letter == "S":
#             return True
#         elif letter == "o" or letter == "O":
#             return True
#         elif letter == "g" or letter == "G":
#             return True
#         elif letter == "r" or letter == "R":
#             return True
#         elif letter == "a" or letter == "A":
#             return True
#         elif letter == "m" or letter == "M":
#             return True
#         else:
#             return False
#
#
# print(is_isogram("Algorism"))

# def binary(decimal):
#     if decimal == 0:
#         return "0"
#
#     y = 0
#     result = []
#     while decimal >= 1:
#         y = decimal % 2
#         result.append(str(y))
#         decimal = int(decimal / 2)
#     result.reverse()
#
#     return ''.join(result)
#
#
# print(binary(0))

# def mean(number):
#     number = list(str(number))
#     result = 0
#     for i in range(len(number)):
#         result += int(number[i])
#     return round(result / len(number))
#

# print(mean(1024))

# def count_vowels(word):
#     word = word.lower()
#     return word.count('a') + word.count('e') + word.count('i') + word.count('u') + word.count('o')

# def integer_boolean(binary_number):
#     binary_number = str(binary_number)
#     result = []
#     for i in range(len(binary_number)):
#         if binary_number[i] == '1':
#             result.append(True)
#         else:
#             result.append(False)
#
#     return result
#
#
# print(integer_boolean(1000001))

# number = 0
# while number < 100:
#     if number % 2 == 1:
#         number += 1
#         continue
#     number += 1
#     print(number)

# for i in range(1, 100, 2):
#     print(i)

# numbers = [2, 4, 6, 8, 10]
#
# for number in numbers:
#     if number % 2 == 1:
#         print("The list contains non odd number")
#         break
# else:
#     print("The list contains only even numbers")

# p = [10, 40, 50]
# p.reverse()

# numbers = []
# while True:
#     user_input = input("Enter a number or if you want to exit, enter 'q': ")
#     if user_input == "q":
#         break
#     numbers.append(int(user_input))
#
# print(numbers)
# print("Max", max(numbers))
# print("Min", min(numbers))

# def nth_smallest(lst, n):
#     lst.sort()
#     if n > len(lst):
#         return None
#     return lst[n-1]
#
#
# numbers = [5, 12, 46, 1]
# print(nth_smallest(numbers, 3))

# def find_odd(lst):
#     result = []
#     for i in lst:
#         if lst.count(i) % 2 == 1:
#             if not result.__contains__(i):
#                 result.append(i)
#     return result
#
#
# numbers = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
# print(find_odd(numbers))


# def probability(lst, num):
#     favourable_outcomes = 0
#     for i in lst:
#         if i >= num:
#             favourable_outcomes += 1
#
#     return round(100 * favourable_outcomes / len(lst), 1)

# def add_indexes(lst):
#     new_list = []
#     for i in enumerate(lst):
#         new_list.append(i[0] + i[1])
#
#     return new_list
#
#
# print(add_indexes([0, -1, -2, -3, -4]))

# def filter_list(lst):
#     result = lst[:]
#     for i in lst:
#         if type(i) is str:
#             result.remove(i)
#     return result
#
#
# print(filter_list([1, 2, "a", "b"]))

# def average(*args):
#     return int(sum(args) / len(args))
#
#
# print(average(1, 5, 2, 3, 67, 12))

# total = 1


# def add(a, b):
#     return a + b + total
#
#
# print(add(1, 2), total)


# def factorial(in_data):
#     if in_data == 1:
#         return 1
#     return factorial(in_data-1)*in_data
#
#
# print(factorial(9))
