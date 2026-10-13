# class School:
#     def __init__(self):
#         print("Constructor of school is called")
#     a=8

# class College(School):
#     def __init__(self):
#         print("COnstructor of college is called")
#     b=4

# class university(College):
#     def __init__(self):
#         super().__init__()
#         print("Constructor of university is called")
#     c=5
# t = university()
# print(t.a,t.b,t.c)

# Parent class
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")


# Child class
class programmer(employee):
    def __init__(self, name, salary, language):
        # Calling parent constructor using super()
        super().__init__(name, salary)

        self.language = language

    def showlanguage(self):
        print(f"{self.name} is good at {self.language}")


# Creating object
p = programmer("Rahul", 80000, "Python")

# Calling methods
p.show()
p.showlanguage()