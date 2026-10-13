#program to determine whether a given name is in list or not.

a=["Alice", "Bob", "Charlie", "David", "Eve"]
name=input("Enter a name: ")
if (name in a):
    print("The name is in the list.")
else:
    print("The name is not in the list.")