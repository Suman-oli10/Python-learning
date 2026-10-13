#program to print names starting with "S" from a list

l={"Suman","Rohit","Sailesh","Hairsh","David"}

for name in l:
    if(name.startswith("S")):
        print(f"Hello, {name}!")