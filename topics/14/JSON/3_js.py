# import json

# x = { 
#     "name":"Liubov", 
#     "age":25, 
#     "city":"Lviv"
#     }

# y = json.dumps(x)
# print("x:", type(x))
# print("Data from JSON---y: ", y)
# print(type(y))                                  

##############
# dict # list # tuple # string # int # float

import json
  
print(json.dumps({"name": "Liubov", "age":  25}))
print(type(json.dumps(["Opel", "BMW"])))
print(json.dumps(("Nissan", "BMW")))
print(json.dumps("hello"))
print(json.dumps(5642))
print(json.dumps(971.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
