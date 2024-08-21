class Person:
    name = "John"
    height = 170
    
    def talk(self):
        print(self.name, "is talking")
        
person = Person()

person2 = Person()

person.talk()

person2.talk()

person.name = "Max"

person2.talk()

person.talk()

print(type(person))