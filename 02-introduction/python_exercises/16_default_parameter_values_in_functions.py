# Create function that uses 1 argument and that argument uses default value as string and print results using
# default and passed argument
def exe1(year="2024"):
    print(year)


# Create function that uses 2 arguments and that arguments uses default values as string and print results using
# default and passed argument.
def exe2(year="2024", season="spring"):
    print(f'{season}, {year}')


# Create method that uses 1 argument and that argument uses default value as string and print results using
# default and passed argument
class Hello:
    def exe3(self, year="2024"):
        print(year)


# Create method that uses 2 arguments and that arguments uses default values as string and print results using
# default and passed argument.

class Collection:
    def exe4(self, year="2024", season="spring"):
        print(f'{season}, {year}')
