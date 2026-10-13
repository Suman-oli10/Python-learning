class employee:
    Company = "Google"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class programmer(employee):
    Company = "Microsoft"
    language = "Python"

    def showlanguage(self):
        print(f"The name is {self.name} and he is good with the language {self.language}")


# Creating object
a = programmer()

# Setting instance attributes
a.name = "Rahul"
a.salary = 80000

# Calling methods
a.showlanguage()
a.show()



#Another example of inheritance:
# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating object of Dog class
d = Dog()

# Accessing parent class method
d.speak()

# Accessing child class method
d.bark()