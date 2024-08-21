class Person:
    name = None
    height = None
    
    def __init__(self, name, height):
        self.name = name
        self.height = height
        print("instantiate", name)
        
    def __del__(x):
        print(x.name, "is being destroyed")
        
    def talk(self, word):
        print(self.name, "is saying", word)
    
    def walk(self):
        print(self.name, "Is walking")
        

john = Person("John Doe", 180)

max = Person("Max Sam", 170)

print(john.name, john.height)

print(max.name, max.height)
    
    
john.talk("Hello")
max.talk("I'm busy")


john.walk()

max.walk()
