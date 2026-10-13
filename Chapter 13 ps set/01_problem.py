#program to filter the numbers which are divisible by 5 from a list of numbers
def division(n):
    if(n%5==0):
        return True
    return False

a=[1,2,3,4,5,6,7,8,9,10]
f=list(filter(division,a))
print(f)
 
 