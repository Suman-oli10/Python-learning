class Employee:
    language="Python"
    salary=50000

    def getinfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    def greet(self):
        print("Hello, welcome to the company!")

harry=Employee()
harry.getinfo()#Employee.getinfo(harry) is also correct but it is not recommended
harry.greet()