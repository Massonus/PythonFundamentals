class InfiniteIterator:
    def __init__(self):
        self.__int = 0

    def __next__(self):
        self.__int += 1
        return self.__int


class InfiniteNumbers:
    def __iter__(self):
        return InfiniteIterator()


infinite_numbers = InfiniteNumbers()

for x in infinite_numbers:
    print(x)

    if x > 99:
        break