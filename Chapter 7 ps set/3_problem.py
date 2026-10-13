#program to print the multiplication table of a given number using while loop.


n=int(input("Enter a number:"))

i=1
while i<=10:
    print(f"{n} * {i} = {n*i}")
    i+=1