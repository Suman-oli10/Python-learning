#program to make a copy of a file
with open("this.txt") as f:
    content=f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)
