# program to find whether a given username contains less than 10 characters or not.

username=input("Enter your username: ")
if(len(username)<10):
    print("Your username is valid.")
else:
    print("Your username is not valid.")