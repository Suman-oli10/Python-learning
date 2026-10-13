#program to find the square, cube and square root of a number using class and object
class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")

    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")

    def square_root(self):
        print(f"The square root of {self.n} is {self.n**0.5}")

c = calculator(3)
c.square()
c.cube()
c.square_root()
