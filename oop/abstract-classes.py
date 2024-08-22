class Car:
    speed = 0
    def accelerate(self):
        pass
    
car = Car()
car.accelerate()
print(car.speed)

class Ferari(Car):
    def accelerate(self):
        self.speed += 30
        
ferari = Ferari()

ferari.accelerate()

print(ferari.speed)