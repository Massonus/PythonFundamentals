# generator version

def fib(n):
    fib_1 = fib_2 = 1
    for i in range(n):
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2


for x in fib(15):
    print(x)


########################3
#without generator

# def fib(n):
#     fib_1 = fib_2 = 1
#     result = []
#     for i in range(n):
#         result.append(fib_1)
#         fib_1, fib_2 = fib_2, fib_1 + fib_2
#     return result

# print(fib(100))