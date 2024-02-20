class Vehicle:
    def set_speed(self, speed):
        self.speed = speed
class Car(Vehicle):
    def __init__(self, brand, speed = 0):#when we move from class to object we call the init method
        self.car_brand = brand
        self.speed = 0                    #self is the object itself

class Ferrari(Car):
    def __init__(self):
        #we need to call the init of the mother class
        super().__init__("Ferrari", 100)
        self.music = "classic"

    def make_cabrio(self):
        self.speed = 20
        self.music = "loud"
        return "wow"


mycar = Car("Renault")
yourcar = Ferrari()
print(yourcar.car_brand)
yourcar.set_speed(120)
print(yourcar.speed)

print(yourcar.make_cabrio(), "and music is", yourcar.music, "and speed is", yourcar.speed)