#program to find where the word "python" is present in which line of the file:
with open("log.txt") as f:
    lines=f.readlines()

lineno=1    
for line in lines:
    if("python" in line):
        print(f"python is present in line number {lineno}")
    lineno+=1
    break
else:  
    print("no python is present in the file")