#program to find the greatest number in a list using reduce function
from functools import reduce

l = [12, 3434, 12, 34, 23424, 23, 12, 23]

def greater(a, b):
    if a > b:
        return a
    else:
        return b

print(reduce(greater, l))