#program to read a file and check if the word "python" is present in the file or not
with open("log.txt","r") as f:
    content=f.read()

if("python" in content):
    print("yes")
else:    print("no")