# Question 18: Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.

personal = {
    'name': 'Junth',
    'age': 21
    }
print(personal)
# {'name': 'Junth', 'age': 21}

# Serialization: Dict to JSON
import json
encode = json.dumps(personal)
print(encode)
# {"name": "Junth", "age": 21}

# Deserialization: JSON to Dict
decode = json.loads(encode)
print(decode)
# {'name': 'Junth', 'age': 21}
