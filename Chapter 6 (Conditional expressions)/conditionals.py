#IF-ELSE-elif ladder:

age=int(input("Enter your age: "))
if (age<18):
    print("You are a minor.")
    print("YOu are not elligible")

elif(age>=100):
    print("Invalid age")

elif(age==0):
    print("The age cannot be zero")

else:
    print("You are an adult.")
    print("You are elligible")   

print("End of the program  ")