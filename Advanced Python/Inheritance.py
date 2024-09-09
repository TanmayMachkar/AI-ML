class Vehicle:
    def general_usage(self):
        print("General use: transportaion")
        
class Car(Vehicle):
    def __init__(self):
        print("I'm a car")
        self.wheels = 4
        self.has_root = True
        
    def specific_usage(self):
        self.general_usage()
        print("specific usage: commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm a motor cycle")
        self.wheels = 2
        self.has_root = False
    
    def specific_usage(self):
        print("specific usage: road trip, racing")
        
c = Car()
c.specific_usage()

m = MotorCycle()
m.specific_usage()
