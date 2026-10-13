# Create a class Programmer for storing information of programmers working in a company. It should have the following attributes and methods:
# Attributes: name, salary, id
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary,id):
        self.name = name
        self.salary = salary
        self.id = id

    def getDetails(self):
        return f"The name of the programmer is {self.name}\n His/Her salary is {self.salary} and id is {self.id}"

p=Programmer("Bill", 100000, 87)
print(p.getDetails())