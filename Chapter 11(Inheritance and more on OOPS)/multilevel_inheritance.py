class School:
    def teaching(self):
        name = "Tapesh"
        print(f"{name} is teaching math subject in school")

class College(School):
    def teaching(self):
        name = "Ganesh"
        print(f"{name} is teaching physics subject in college")

class university(College):
    def teaching(self):
        name = "Ramesh"
        print(f"{name} is teaching computer science subject in university")

t = university()
a = School()
b = College()
t.teaching()
a.teaching()
b.teaching()