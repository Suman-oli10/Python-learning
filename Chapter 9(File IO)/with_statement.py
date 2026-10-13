f=open("file.txt")
print(f.read())
f.close()

# Better way to read a file using with statement
with open("file.txt") as f:
    print(f.read())

#we don't need to close the file when we use with statement
#  it will automatically close the file after the block of code is executed.