class Person:
    name = "John"
    age = 50
    
    def speak(self):
        print(self.name, "is speaking")
        
    def grow(self):
        self.age += 1
        

person = Person()

person2 = Person()

person2.name = "Mike"

print(person.name, person2.name)

person2.age = 20

print(person.age, person2.age)

person.speak()

person2.speak()

person2.grow()

print(person.age, person2.age)

