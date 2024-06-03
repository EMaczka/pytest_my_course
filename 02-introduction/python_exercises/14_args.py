# Create function that uses *args and will print result of adding 5 integers
def add(*args):
    print(sum(args))


# Create function that uses one string parameter and *args, and will print that parameter with args
def print_func(word: str, *args):
    sec_part = ''
    for arg in args:
        sec_part += f'{arg} '
    print(f'{word} {sec_part}')
