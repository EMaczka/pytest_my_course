# Create simple dictionary which key and value will be strings
dict1 = {"hello": "ciao", "hi": "salve", "husband": "marito"}
# Create dictionary which wil use keys: name, age, city. Values of those keys should be string/int/string.
# Print value for name and age
dict2 = {"name": "Pedro", "age": 2, "city": "Amalfi"}
print(dict2["name"])
print(dict2["age"])
# Create dictionary which will use keys: name, age, city. Values of those keys should be string/int/string.
# Change name and then print it
dict3 = {"name": "Pedro", "age": 2, "city": "Sorrento"}
dict3["name"] = "Francesco"
print(dict3["name"])
# Create dictionary which will use keys: name, age, city. Values of those keys should be string/int/string.
# Delete name and then print it
dict4 = {"name": "Pedro", "age": 2, "city": "Parma"}
del dict4["name"]
print(dict4)
# Create dictionary which will use keys: name, age, city. Values of those keys should be string/int/string.
# Print every key in that dictionary
dict5 = {"name": "Pedro", "age": 2, "city": "Trevisto"}
for i in dict5:
    print(i)
# Create dictionary which will use keys: name, age, city. Values of those keys should be string/int/string.
# Print every value in that dictionary
dict6 = {"name": "Pedro", "age": 2, "city": "Positano"}
for i in dict6.values():
    print(i)
# Create dictionary which will use keys: name, age, city. Values of those keys should be string/int/string.
# Print all items in that dictionary
dict7 = {"name": "Pedro", "age": 2, "city": "Napoli"}
for key, value in dict7.items():
    print(key, value)
