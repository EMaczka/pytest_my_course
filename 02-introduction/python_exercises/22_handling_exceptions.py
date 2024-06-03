# Create correct try/except block for below code and print error message
try:
    result = 10 / 0
    print(result)
except Exception as e:
    print(str(e))

# Create correct try/except block for ZeroDivisionError and TypeError for below code and print error message
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError as e2:
    print(str(e2))
except TypeError as e3:
    print(str(e3))

# Create correct try/except block for all exception and print error message
try:
    list1 = [0, 1]
    print(list1[2])
except Exception as e4:
    print(f'error occurred: {e4}')

# Create correct try/except/finally block for all exception, print error message and message for finally block
try:
    result = 10 / 0
    print(result)
except Exception as e5:
    print(e5)
finally:
    print('Operation has been finished')
