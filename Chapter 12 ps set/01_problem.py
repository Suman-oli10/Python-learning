 #program to open three files and if these files are not found write a message without exiting the program:
try:
    with open("file1.txt", "r") as f:
        print(f.read())
except:
    print("Error occurred while reading the file.")


try:
    with open("file2.txt", "r") as f:
        print(f.read())

except:
    print("Error occurred while reading the file.")

try:
    with open("file3.txt", "r") as f:
        print(f.read())

except:
    print("Error occurred while reading the file.")

finally:
    print("All files read successfully.")