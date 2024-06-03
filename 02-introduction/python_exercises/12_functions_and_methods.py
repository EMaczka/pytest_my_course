# Create function that will print text variable
def print_text(i):
    print(i)


text = "Some text"
print_text(text)


# Create method that will print another_text
class Exercise:
    def print_text(self, i):
        print(i)


another_text = "Another text"
instance = Exercise()
instance.print_text(another_text)
