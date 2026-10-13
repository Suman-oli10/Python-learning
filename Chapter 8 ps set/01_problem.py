#program to find the greatest of three numbers using function:
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
print(f"The greatest number is: {greatest(a, b, c)}")
