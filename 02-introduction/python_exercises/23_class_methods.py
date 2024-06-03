# Create class and method in that class that will print message, create instance of that class and call the
# method from that instance
class Exercise1:
    def print_hello(self):
        print("Hello")


exe1 = Exercise1()
exe1.print_hello()


# Create class, variable and methods that will set variable, return variable. Use those methods to set variable to
# integer, and print that variable.
class Exercise2:
    variable1 = None

    def set_value(self, value):
        self.variable1 = value

    def get_value(self):
        return self.variable1


exe2 = Exercise2()
exe2.set_value(2024)
print(exe2.get_value())


# Create class, static variable and methods that will set that variable, return variable. Use those methods to set
# variable to integer, and print that variable
class Exercise3:
    static_variable = None

    def set_value(self, value):
        Exercise3.static_variable = value

    def get_value(self):
        return Exercise3.static_variable


exe3 = Exercise3()
exe3.set_value(2024)
print(exe3.get_value())


# Create class, static variable and static methods that will set that variable, return variable.
# Use those methods to set variable to integer, and print that variable
class Exercise4:
    static_variable = None

    @staticmethod
    def set_value(value):
        Exercise4.static_variable = value

    @staticmethod
    def get_value():
        return Exercise3.static_variable


Exercise4().set_value(2024)
print(Exercise4.get_value())
