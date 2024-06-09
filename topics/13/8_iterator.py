# Кожен об'єкт, що може бути ітерованим, 
# повинен мати метод __iter__, 
# що повертає ітератор.
# Ітератор повинен мати метод __next__, 
# що повертає наступне значення при 
# кожному виклику. Коли значення закінчаться, 
# буде викинуто виключення StopIteration.
# Ітератор також повинен мати метод __iter__, 
# що повертає сам ітератор.

# ітератори зберігають стан, 
# і тому, закінчивши ітерацію один раз, 
# його стан зберігається. В цьому і плюс 
# ітерованих об'єктів: 
# кожен раз повертати новий ітератор, 
# що і роблять вбудовані типи (наприклад, list).


# class HundredIterator:
#     def __init__(self):
#         self.__int = 0

#     def __next__(self):
#         if self.__int > 99:
#             raise StopIteration

#         self.__int += 1
#         return self.__int


# one_hundred = HundredIterator()

# for x in one_hundred:
#     print(x)

# Traceback (most recent call last):
#   File "iter.py", line 15, in <module>
#     for x in one_hundred:
# TypeError: 'HundredIterator' object is not iterable

class HundredIterator:
    def __init__(self):
        self.__int = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__int > 99:
            raise StopIteration

        self.__int += 1
        return self.__int


one_hundred = HundredIterator()

for x in one_hundred:
    print(x)
