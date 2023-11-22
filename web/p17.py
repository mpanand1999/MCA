#Merge two dictionaries

dict1 = {"name": "Alice", "age": 25}
dict2 = {"name":"ammu","occupation": "Software Engineer", "hobbies": ["reading", "writing", "coding"]}


# Merge dict2 into dict1
print(dict1)
dict1.update(dict2)
print(dict1)
