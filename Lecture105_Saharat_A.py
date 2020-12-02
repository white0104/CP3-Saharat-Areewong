class Vehicle :
    licenseNumBer = ""
    serialCode = ""
    def turnOnAirConditioner(self) :
        print("Turn on Air")
class Car(Vehicle):
    pass
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
car1 = Car()
car1.turnOnAirConditioner()
pickup1 = Pickup()
pickup1.turnOnAirConditioner()
Van1 = Van()
Van1.turnOnAirConditioner()
