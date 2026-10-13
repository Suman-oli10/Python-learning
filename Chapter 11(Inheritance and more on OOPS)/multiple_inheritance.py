# First parent class
class employee:
    Company = "Google"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


# Second parent class
class manager:
    department = "IT"

    def showdepartment(self):
        print(f"{self.name} works in {self.department} department")


# Child class inheriting from both employee and manager
class programmer(employee, manager):
    Company = "Microsoft"
    language = "Python"

    def showlanguage(self):
        print(f"The name is {self.name} and he is good with the language {self.language}")


# Creating object
a = programmer()

# Setting instance attributes
a.name = "Rahul"
a.salary = 80000

# Calling methods from all classes
a.showlanguage()      # programmer class
a.show()              # employee class
a.showdepartment()    # manager class