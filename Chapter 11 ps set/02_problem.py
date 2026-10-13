class Animals:
    def sound(self):
        print("Animals make sound")

class Pets(Animals):
    def sound(self):
        print("Pets make sound")

class Dog(Pets):
    def bark(self):
        print("Dogs bark")

d=Dog()
d.bark()
d.sound()
