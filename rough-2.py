class Person:
    name = None
    age = None
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
    def speak(self):
        print(self.name, "is speaking")
        
    def grow(self):
        self.age += 1
        
        

person = Person("Mike", 60)

class PoliceMan(Person):
    def arrest(self):
        print(self.name, "is arrested an offender")

police = PoliceMan("Joe", 30)

police.speak()

police.grow()

print(police.age)

police.arrest()

class Sarz(PoliceMan):
    def plait_dread(self):
        print(self.name, "just plaited dreadlocks")
        
sarz = Sarz("Sam", 32)

sarz.plait_dread()