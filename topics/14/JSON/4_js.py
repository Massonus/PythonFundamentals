import json

data = { 
    "name":"Liubov", 
    "age":35, 
    "city":"Lviv",
    "children": [
        {
        "name": "Maksym",
        "age": 6
        }  
    ]
}

# with open("create_data_file.json", "w") as write_file:
#     json.dump(data, write_file)

with open("create_data_file_indent.json", "w") as write_file:
    json.dump(data, write_file, indent = 4)


