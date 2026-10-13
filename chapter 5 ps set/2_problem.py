#program to input 5 numbers from the user and display all the unique number once.

s=set()
n=input("Enter number of elements: ")
s.add(int (n))
n=input("Enter number of elements: ")
s.add(int (n))
n=input("Enter number of elements: ")
s.add(int (n))      
n=input("Enter number of elements: ")
s.add(int (n))
n=input("Enter number of elements: ")
s.add(int (n))
print(s)