import re

# pattern = "Hello SoftServe IT Academy"


# result_1 = re.match(r"Hello", pattern)
# # result_2 = re.match(r"it", pattern)
# # result_3 = re.match(r"IT", pattern)

# print(result_1)
# print(result_1.group())

# print(result_2)



# print(result_3)


# # #################################################

# import re

# pattern = "SoftServe IT Academy, Hello, Python"


# result_1 = re.search(r"Hello", pattern)
# result_2 = re.search(r"it", pattern)
# result_3 = re.search(r"IT", pattern)

# print(result_1)
# print(result_1.group())


# print(result_2)
# print(result_3)


################################################
# import re

# pattern = "SoftServe IT Academy, Hello, IT, IT Python"


# result_1 = re.findall(r"Hello", pattern)
# result_2 = re.findall(r"it", pattern)
# result_3 = re.findall(r"IT", pattern)

# print(result_1)
# print(result_2)
# print(result_3)
# ###############################################
# import re

# pattern = re.compile('IT')

# result_1 = re.compile('IT').findall(r"IT SoftServe")
# print(result_1)

# result_2 = pattern.findall(r"IT SoftServe IT Python IT")
# print(result_2)

##################################################################


# import re

# pattern = "SoftServe IT Academy Hello IT IT Python"


# result_1 = re.split("e", pattern)
# result_2 = re.split("IT", pattern)

# result_3 = re.split("e", pattern)
# result_4 = re.split("e", pattern, maxsplit=2)

# print(result_1)
# print(result_2)
# print(result_3)
# print(result_4)
# #############################################

# import re

# pattern = "SoftServe IT Academy Hello IT IT Python IT"


# result_1 = re.sub("e", "@", pattern)
# result_2 = re.sub("IT", "#", pattern, count=2)
# result_3 = re.sub("IT", "%", pattern)

# print(result_1)
# print(result_2)
# print(result_3)

# ################################################
# import re

# pattern = "SoftServe IT Academy Hello IT IT Python IT 2020"


# result_1 = re.findall("[a-m]", pattern)
# result_2 = re.findall("\d", pattern)

# print(result_1)
# print(result_2)



# #########################################
# import re

# pattern = "Hello SoftServe  Hello IT Academy Sowertyve"


# result_1 = re.findall("So.....ve", pattern)
# result_2 = re.findall("^Hello", pattern)
# result_3 = re.findall("Hello$", pattern)

# print(result_1)
# print(result_2)
# print(result_3)



##########################################
import re

pattern = "Hello SoftServe IT Academy IT SoftServe every day helli ely"

#Check if the string contains "er" followed by 0 or more "x" characters:
result_1 = re.findall("erx*", pattern)


#Check if the string contains "e" followed by exactly two "l" characters:
result_2 = re.findall("el{2}", pattern)

#Check if the string contains either "IT" or "day":
result_3 = re.findall("IT|day", pattern)

print(result_1)
print(result_2)
print(result_3)



