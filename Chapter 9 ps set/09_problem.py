#program to compare two files whether they are identical or not:
with open ("file.txt") as f: #file1
    content1=f.read()

with open ("poem.txt") as f: #file2
    content2=f.read()

if content1==content2:
    print("They are identical")
else:    
    print("They are different")



#Identical case:
with open ("this.txt") as f: #file1
    content1=f.read()

with open ("this_copy.txt") as f: #file2
    content2=f.read()

if content1==content2:
    print("They are identical")
else:    
    print("They are different")