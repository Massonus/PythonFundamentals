# def get_count(sentence):
#     return sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')
#
#
# print(get_count("string"))


# def maskify(number):
#     number = list(str(number))
#     for i in range(len(number)-4):
#         number[i] = '#'
#     return ''.join(number)
#
#
# print(maskify("123456456873"))
#

# def disemvowel(string_: str):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for char in string_:
#         if char.lower() in vowels:
#             string_ = string_.replace(char, '')
#     return string_
#
#
# print(disemvowel("This website is for losers LOL!"))

# def likes(names: list):
#     if len(names) == 1:
#         return f'{names[0]} likes this'
#     elif len(names) == 2:
#         return f'{names[0]} and {names[1]} like this'
#     elif len(names) == 3:
#         return f'{names[0]}, {names[1]} and {names[2]} like this'
#     elif len(names) >= 4:
#         return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
#     else:
#         return 'no one likes this'

# def high(x: str):
#     letter_scores = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
#                      'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
#                      'x': 24, 'y': 25, 'z': 26}
#
#     string = x.split(' ')
#     result_dict = {}
#     for item in string:
#         letter_sum = 0
#         for letter in list(item):
#             letter_sum += letter_scores[letter]
#         result_dict.update({item: letter_sum})
#     return max(result_dict, key=result_dict.get)
#
#
# print(high('aa b'))

# def spin_words(sentence: str):
#     sentence = sentence.split(" ")
#     for word in sentence:
#         if len(word) >= 5:
#             sentence[sentence.index(word)] = word[::-1]
#
#     return " ".join(sentence)
#
#
# print(spin_words("Welcome"))

# def find_outlier(integers: list):
#     even = 0
#     odd = 0
#     for number in integers:
#         even += 1 if number % 2 == 0 else 0
#         odd += 1 if number % 2 != 0 else 0
#
#     if even > odd:
#         for number in integers:
#             if number % 2 != 0:
#                 return number
#     else:
#         for number in integers:
#             if number % 2 == 0:
#                 return number
#
#
# print(find_outlier([1, 0, 0]))

# def find_it(seq: list):
#     dict_result = {}
#     for i, item in enumerate(seq):
#         dict_result.update({item: dict_result.get(item, 0) + 1})
#
#     for key, value in dict_result.items():
#         if value % 2 != 0:
#             return key
#
#
# print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))

# def array_diff(a: list, b: list):
#     result = []
#     for item in a:
#         if item not in b:
#             result.append(item)
#     return result
#
#
# array_diff([1, 2, 3], [1, 2])

# def order(sentence: str):
#     dict_position = {}
#     sentence_list = sentence.split()
#     for word in sentence_list:
#         for letter in word:
#             if letter.isnumeric():
#                 dict_position.update({word: letter})
#
#     dict_position = {k: v for k, v in sorted(dict_position.items(), key=lambda item: item[1])}
#     return " ".join(list(dict_position.keys()))
#
# # v2
# def order(words):
#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
#
# print(order("is2 Thi1s T4est 3a"))


# def tower_builder(n_floors):
#     result = []
#     for floor in range(n_floors):
#         spaces = ' ' * (n_floors - floor - 1)
#         stars = '*' * (2 * floor + 1)
#         result.append(spaces + stars + spaces)
#     return result
#
#
# tower = tower_builder(5)
# for i in tower:
#     print(i + '\n')
