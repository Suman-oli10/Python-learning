class Employee:
    a=6
    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")

e=Employee()
e.a=45
Employee.show()
