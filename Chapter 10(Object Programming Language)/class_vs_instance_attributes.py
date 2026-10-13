class Employee:
    language="Python"#class attribute
    salary=50000

harry=Employee()
harry.language="Java"#instance attribute
print(harry.language,harry.salary)

#Instance attribute takes preferece over class attribute if both are present with same name.