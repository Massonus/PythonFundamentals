# with open("firstfile.txt", "r") as my_file:
#     print("first call cursor:", my_file.tell())
#     str1 = my_file.read(5)
#     print("seconds call cursor:", my_file.tell())
#     print(str1)

#     str2 = my_file.read(7)
#     print("second call cursor:", my_file.tell())
#     print(str2)
    
    
#     print(my_file.tell())


# # #     ############
#     print(str1, end="#")
# #     ##############
#     print(str2, end="\n")


# ##############################
# with open("firstfile.txt", "r") as my_file:
#     str1 = my_file.readline()
   
#     print(str1)
    
# # # # 


# # ##################################
# with open("firstfile1.txt", "r") as my_file:
#     str1 = my_file.readlines()
#     print(str1)
#     print(str1[1])
# # # # # # # # # # # # ##
#     print(my_file.tell())
# # # # # # # # # # #######
#     my_file.seek(0) 
#     print(my_file.tell())
    
    


# ########################################
# my_file = open("second.txt", 'r')
# for item in my_file:
#     print(item)
# my_file.close()


# ######################################
# my_file = open("second.txt", 'w')
# my_file.write("Hello Python\nITAcademy\nSoftServe")
# my_file.close()

# ########################
# with open("second.txt", "r") as file:
#     for line in file:
#         print(line, end="")

