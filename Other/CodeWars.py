# def get_count(sentence):
#     return sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')
#
#
# print(get_count("string"))


def maskify(number):
    number = list(str(number))
    for i in range(len(number)-4):
        number[i] = '#'
    return ''.join(number)


print(maskify("123456456873"))

