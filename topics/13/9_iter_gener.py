# iterator
# class SimpleIterator:
#     def __iter__(self):
#         return self

#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0

#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return 1
#         else:
#             raise StopIteration

# s_iter2 = SimpleIterator(5)
# for i in s_iter2:
#     print(i)

##################
# generator
##################

def simple_generator(val):
   while val > 0:
       val -= 1
       yield val

# gen_iter = simple_generator(5)
gen_iter = simple_generator(7)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
