class InfiniteIterator:
    def __init__(self):
        self.__int = 0

    def __next__(self):
        self.__int += 1
        return self.__int

inf_iter = InfiniteIterator()

print(next(inf_iter))
print(next(inf_iter))
print(next(inf_iter))
print(next(inf_iter))