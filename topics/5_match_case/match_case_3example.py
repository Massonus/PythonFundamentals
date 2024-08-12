# def load(input_data):
#     print(f"From load {input_data}")

# def save(input_data, other):
#     print(f"From save {input_data, other}")

# def default(input_data):
#     print(f"From default {input_data}")

# DATA_STRING_1 = "load~http://example.com/file/testpython.txt~test.txt"
# DATA_STRING_2 = "save~http://example.com/file/testpython.txt~test.txt"
DATA_STRING_3 = "save~http://example.com/file/testpython.txt~test.txt~test2.txt~test3.txt"

values = DATA_STRING_3.split("~")
print(values)

match values:
    case "load", link:
        #load(link)
        print(link)
    case "save", link, filename:
        #save(link, filename)
        print(link, filename)
    case "save", link, *filenames:
        for filename in filenames:
            #save(link, filename)
            print(link, filenames)
    case _:
        #default(values)
        print("another")

   

