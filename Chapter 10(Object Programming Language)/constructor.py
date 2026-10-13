class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object
p1 = Person("Alice", 25)

p1.show()