# Create variable which will take none as a value and print it
var = None
print(var)


# Create function that will return none
def return_none():
    return None


# Create function that will return none only if passed argument is empty string
def return_none_if(arg):
    if arg != "":
        return not None
    else:
        return None


# Create function that will check if passed argument is none type object
def check_arg(arg):
    if arg is None:
        print("argument is None")
    else:
        print("argument is not None")
