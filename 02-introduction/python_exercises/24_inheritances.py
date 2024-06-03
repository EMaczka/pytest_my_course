# Create class animal and method speak which will print message
class Animal:
    def speak(self):
        print("Animal speaking")


# Create class dog with method bark. Make dog inherit after class animal and use methods from animal and dog
class Dog(Animal):
    def bark(self):
        print("Woof!")


dachshund = Dog()
dachshund.speak()
dachshund.bark()


# Create class cat with method speak. Make cat inherit after class animal and use method speak
class Cat(Animal):
    def speak(self):
        print("Meow!")


tricolor = Cat()
tricolor.speak()


# Create class horse with method speak which will use "super" method to use it after inheriting from animal
class Horse(Animal):
    def speak(self):
        super().speak()
