# def decorator_function(func):
#     def wrapper():
#         print('Outer function!')
#         func()  # call inner function
#         print('Exit from outer function')
#     return wrapper




# @decorator_function
# def hello_world():
#     print('Hello world!')

# hello_world()

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner
    
def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
# @star
@percent
def printer(msg):
    print(msg)

printer("Hello")

