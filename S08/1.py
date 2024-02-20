class Car:
    def __init__(self, brand):#when we move from class to object we call the init method
        self.brand = brand
        self.speed = 0                    #self is the object itself


    def set_speed(self, speed):
        self.speed = speed
    def get_speed(self):
        return self.speed

    def get_brand_nationality(self):
        if self.brand == "Renault":
            return "France"
        elif self.brand == "Ferrari":
            return "Italy"

    def set_age(self, age):
        self.age = age

    def set_value(self, value):
        self.value = value


mycar = Car("Renault")

mycar.set_speed(80)
print(mycar.speed)
print(mycar.get_brand_nationality())

yourcar = Car("Ferrari")
print(yourcar.speed)