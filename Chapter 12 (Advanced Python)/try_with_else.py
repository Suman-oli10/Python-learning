try:
    a=int(input("Hey! Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("This block will only run if try block is successful and no exception is raised")
 