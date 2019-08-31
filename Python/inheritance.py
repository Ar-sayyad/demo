class Vehicle:
    def general_usage(self):
        print("general use: transportation")


class Car(Vehicle):
    def __init__(self):
        print("I am car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work & so on..")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I am motor Cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific use: racing..")


c = Car()
#c.specific_usage()
m = MotorCycle()
#m.specific_usage()
print(isinstance(c,Car))