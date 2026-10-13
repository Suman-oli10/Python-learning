#program to read a file and replace the words "donkey","pagal","rough","bad","ugly" with "######"
words=["donkey","pagal","rough","bad","ugly"]

with open("newfile.txt","r") as f:
    content=f.read()
    
for word in words:
    content=content.replace(word,"#" * len(word))
with open("newfile.txt","w") as f:
    f.write(content)