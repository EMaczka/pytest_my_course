# Create set of numbers from 1 to 5
set1 = {1, 2, 3, 4, 5}
# Create a set of numbers from 1 to 5 and add number 6 to that set
set2 = {1, 2, 3, 4, 5}
set2.add(6)
# Create a set of numbers from 1 to 5 and remove number 2 from that set
set3 = {1, 2, 3, 4, 5}
set3.remove(2)
# Create a set of numbers from 1 to 5 and print how many elements are in that set
set4 = {1, 2, 3, 4, 5}
print(len(set4))
# Create a set of numbers from 1 to 5 and check if number 3 is in that set
set5 = {1, 2, 3, 4, 5}
print(3 in set5)
# Create two sets, first one with numbers from 1 to 5. Second one with numbers from 4 to 8. Print
# differences between them
set6 = {1, 2, 3, 4, 5}
set7 = {4, 5, 6, 7, 8}
print(set6.difference(set7), set7.difference(set6))
# Create frozen set of numbers from 1 to 5
set8 = frozenset([1, 2, 3, 4, 5])
