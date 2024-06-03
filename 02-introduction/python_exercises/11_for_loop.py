# Create for loop that will print every element from the list
list_of_numbers = [1, 2, 3, 4, 5, 6]

for elem in list_of_numbers:
    print(elem)

# Create for loop that will print numbers from 0 to 200
for i in range(201):
    print(i)

# Create for loop that will print numbers between 20 and 40
for i in range(21, 40):
    print(i)

# Create for loop that will print every letter in variable string_variable
string_variable = "This is text"
for char in string_variable:
    print(char)

# Create for loop that will print keys in variable dict_variable
dict_variable = {"a": 1, "b": 2, "c": 3, "d": 4}

for key in dict_variable:
    print(key)

# Create for loop that will be using 2 variables and will print key and value pair from another_dict_variable
another_dict_variable = {"e": 5, "f": 6, "g": 7, "h": 8}

for key, value in another_dict_variable.items():
    print(key, value)

# Create for loop that will create list of numbers from 0 to 100 in variable hundred_element_list
hundred_element_list = []
for i in range(0, 101):
    hundred_element_list.append(i)

print(hundred_element_list)
