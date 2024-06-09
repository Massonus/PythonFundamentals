FILENAME = "file_messages.txt"

messages = list() 

for i in range(5):
    message = input("Enter line" + str(i+1) + ":")
    messages.append(message + "\n")

with open(FILENAME, "a") as my_file:
    for message in messages:
        my_file.write(message)

print("Read messages:")
with open(FILENAME, "r") as my_file:
    for message in my_file:
        print(message, end="")







