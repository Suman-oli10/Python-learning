#program to create a class 2Dvector and use it create another class representing 3D vector. Use the show method to display the vector in both cases.
class TwoDvecotr:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
     print(f"The 2D vector is {self.i}i + {self.j}j")

class ThreeDvector(TwoDvecotr):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The 3D vector is {self.i}i + {self.j}j + {self.k}k")


v1 = TwoDvecotr(2,3)
v2 = ThreeDvector(2,3,4)
v1.show()
v2.show()