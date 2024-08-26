class Person:
    name = None
    age = None
    
    def __init__(self, name, age):
        print("INIT")
        self.name = name
        self.age = age
        
    
    def speak(self):
        print(self.name, "is speaking")
        
    def grow(self):
        self.age += 1
        
    def __del__(self):
        print(self.name, "is destroyed")
        
        
person = Person("John", 15)

person2 = Person("Max", 20)

person.speak()

person2.speak()

del person2

print("Hello")