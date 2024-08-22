from abc import ABC, abstractmethod

class Car(ABC):
    speed = 0
    
    @abstractmethod
    def accelerate(self):
        pass
    

class Ferari(Car):
    def accelerate(self):
        self.speed += 30
        
ferari = Ferari()

ferari.accelerate()

print(ferari.speed)