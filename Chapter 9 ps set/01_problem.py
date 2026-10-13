#program to read a file and check if the word "Twinkle" is present in the file or not
f=open("poem.txt")
content=f.read()
if("Twinkle" in content):
    print("yes")
else:
    print("no")
f.close()