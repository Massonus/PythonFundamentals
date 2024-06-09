import json
from pprint import pprint

json_string = """
{
    "firstName": "Ivan",
    "lastName": "King",
    "hobbies": ["reading", "traveling", "singing"],
    "age": 33,
    "children": [
        {
            "firstName": "Vira",
            "age": 3
        },
        {
            "firstName": "Maksym",
            "age": 5
        }
    ]
}
"""
 
data = json.loads(json_string)

print(data)
pprint(data)
