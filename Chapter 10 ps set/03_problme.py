#progarm to check whether certain condition changes class attribute or not:

class Demo:
    a=4

o=Demo()
print(o.a) #prints the class attribute value (4) because instance attribute is not set yet
o.a=5#instance attribute is set
print(o.a) #prints the instance attribute value 5 because instance attribute has higher priority than class attribute