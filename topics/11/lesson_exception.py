

# print("hello")

class CustomError(Exception): 
    def __init__(self, data): 
        self.data = data
    def __str__(self):
        return repr(self.data)

total_score = int(input("Enter expert score: "))

try:
    num_of_group = int(input("Enter number of your group: "))
    if num_of_group < 1:
        raise CustomError("Number of your group can't be less than 1")
except CustomError as e:
    print("We obtain error:", e.data)   
except ValueError as e:
    print(e)





# print(int("10"))




# print( 2 + "1" )

# print(int("qverty"))
# print(int("10"))
##синтаксична помилка
# for i in range(10)
#     pass




# try:
#     input_param = int(input("Enter your number: "))
#     a = 10/input_param
# except:
#     print(f"Ops!!!Error.")


     



###########################
# prin("hello!")

# ########
# # Traceback (most recent call last):
# #   File "<pyshell#2>", line 2, in <module>
# #     prin("hello!")
# # NameError: name 'prin' is not defined

# #####

# try:
#     a = 100
#     b = 0
#     c = a / b
# except ArithmeticError:
#     print("Error Arithmetic")
# except ZeroDivisionError as e:
#     print(e)


# a=100
# b=0
# c=a/b
# print(c)
########################
# try:
#     a = 100
#     b = 0
#     c = a / d
# except ZeroDivisionError as e:
#     print(e)



#     # #прокидання вийнятку вище
#     try:
#     your_code
# except Exception as e:
#     raise

#     # власні винятки
#     class MyException(Exception):
#         pass
#     raise MyException(Exception)

#     ##########перечислюємо винятки
# print("start")
# try:
#    val = int(input("input number: "))
#    tmp = 10 / val
#    print(tmp)
# except(ValueError, ZeroDivisionError):
#    print("Error!")
# print("stop")

# # ######розділяємо винятки

# print("start")
# try:
#   value = int(input("input number: "))
#   result = 10 / value
#   print(result)

# except ValueError:
#    print("ValueError!")
# except ZeroDivisionError as e:
#    print("Zero")
# except ArithmeticError as e:
#     print("Arith")
# except:
#    print("Error!")
# print("stop")

#######################
# print("start")
# try:
#    val = int(input("input number: "))
#    tmp = 10 / val
#    print(tmp)
# except ValueError:
#    print("ValueError!")
# except ZeroDivisionError:
#    print("ZeroDivisionError!")
# except ArithmeticError:
#    print("ArithmeticError!")
# except:
#    print("Error!")
# print("stop")


# ##########finaly
# try:
#    val = int(input("input number: "))
#    tmp = 10 / val
#    print(tmp)
# except:
#    print("Exception")
# finally:
#    print("Finally code")

  #######примусова генерація винятків


# try:
#   a = int(input("Enter your number: "))

#   if a <= 0:
#     raise ZeroDivisionError("Some exception: negative number")

# except ZeroDivisionError as e:
#     print("!!!Exception exception!!! ", e)

# try:
#    a=int(input("Enther your number: "))
#    if a==0:
#        raise ZeroDivisionError("Divided Zero")
# except ZeroDivisionError as e:
#    print("!!!Exception exception!!! ", e)


# class CustomError(Exception): 
    
#     def __init__(self, data): 
#       self.data = data
    
#     def __str__(self):
#       return repr(f"My repr: {self.data}")


# try:
#     num_of_group = int(input("Enter number of your group: "))
    
#     if num_of_group < 1:
#         raise CustomError("Number of your group can't be less than 1")

# except CustomError as e:
#     print("We obtain error:", e.data)   



