# Create function that will use **kwargs as parameter and will print all kwargs value
def print_kwargs_values(**kwargs):
    for value in kwargs.values():
        print(value)


# Create function that will use **kwargs as parameter and will print all kwargs keys and values
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


# Create function that will use *args and **kwargs as parameters. Function must print all args values and all
# kwargs key values

def print_args_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)
