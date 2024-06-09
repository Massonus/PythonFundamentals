class HundredIterator:
    def __init__(self):
        self.__int = 0

    def __next__(self):
        if self.__int > 99:
            raise StopIteration

        self.__int += 1
        return self.__int


class InfiniteNumbers:
    def __iter__(self):
        return HundredIterator()



one_hundred = InfiniteNumbers()

for x in one_hundred:
    print(x)