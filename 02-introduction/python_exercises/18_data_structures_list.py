# Create list with elements as string/int/float/bool and print it
list1 = ["elem1", 2, 3.12, False]
print(list1)
# Create list of 5 integers and print only second and fifth element
list2 = [21, 43, 1, 22, 99]
print(list2[1], list2[4])
# Create list of 5 integers and print only last element
list3 = [21, 43, 1, 22, 99]
print(list2[-1])
# Create empty list and add two integers to this list, print the results
list4 = []
list4.append(1)
list4.append(4)
print(list4)
# Create two list filled with integers and create new list which is result of adding both of them
list5 = [21, 43, 1, 22, 99]
list6 = [2, 3, 4]
list7 = list5 + list6
# Create list filled with 2 integers and create a new list which is multiplication of this list by 3 times
list8 = [3, 2109]
list9 = list8 * 3
# Create list filled with 5 integers, add number 4 to the list, print the result
list10 = [21, 43, 1, 22, 99]
list10.append(4)
print(list10)
# Create list filled with 5 integers, add number 4 to the list and then sort it, print the result
list11 = [21, 43, 1, 22, 99]
list11.append(4)
list11.sort()
print(list11)
