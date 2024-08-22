class Bird():
    
    name = None
    
    def __init__(self, name):
        self.name = name
        
    def fly(self):
        print(self.name, "is flying")

    
    
bird = Bird("Normal Bird")

bird.fly()

class Hawk(Bird):
    pass

hawk = Hawk("I am Hawk")

hawk.fly()


class Chicken(Bird):
    def fly(self):
        print(self.name, "cannot fly")
    
chicken = Chicken("Chicken")

chicken.fly()