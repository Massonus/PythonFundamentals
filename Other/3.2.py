# def card_hide(card):
#     string_card = str(card)
#     if len(string_card) < 16:
#         return "Invalid card"
#
#     return "************" + string_card[-4:]
#
#
# val = card_hide(124213)
# print(val)

# def divisible_by_five(number):
#     if number % 5 == 0:
#         return True
#     else:
#         return False

# def less_than_100(num1, num2):
#     if num1 + num2 < 100:
#         return True
#     else:
#         return False

# def makes10(num1, num2):
#     if num1 == 10 or num2 == 10:
#         return True
#     elif num1 + num2 == 10:
#         return True
#     else:
#         return False


# def string_int(str1):
#     if not str1.isdigit():
#         return "Not a number"
#
#     return int(str1)
#
#
# print(string_int("1"))

# def X_O(word):
#
#     o = word.count("o") + word.count("O")
#     x = word.count("x") + word.count("X")
#     if o == x:
#         return True
#     elif not o == x:
#         return False
#
#
# X_O("adf")


# def return_negative(number):
#     if number < 0:
#         return number
#
#     return int("-" + str(number))
#
#
# print(return_negative(2))