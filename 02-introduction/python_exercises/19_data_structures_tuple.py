# Create tuple with elements as string/int/float/bool and print it
tup1 = ("tup", 3, 1.23, True)
print(tup1)
# Create tuple of 5 integers and print only second and fifth element
tup2 = (5, 8, 33, 1, 43)
print(tup2[1], tup2[4])
# Create tuple of 5 integers and print only last element
tup3 = (5, 8, 33, 1, 43)
print(tup3[-1])
# Create two tuples filled with integers and create new tuple which is result of adding both of them
tup4 = (5, 8, 33, 1, 43)
tup5 = (22, 17)
tup6 = tup4 + tup5
# Create a tuple which will contain at least four integers with the same value, and print how many times it is in
# that tuple
tup7 = (9, 99, 9, 999, 9999, 99, 9, 99, 9, 999, 9)
print(tup7.count(9))
# Create a tuple with numbers from 1 to 5 and print index of the number 3 in that tuple
tup8 = (1, 2, 3, 4, 5)
print(tup8.index(3))
