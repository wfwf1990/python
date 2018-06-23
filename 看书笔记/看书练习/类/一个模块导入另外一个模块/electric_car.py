# Author: wangfang

from car import Car
class ElectricCar(Car):
    def __init__(self,make,modle,year):
        super(ElectricCar, self).__init__(make,modle,year)
        self.battery_size = Battery()

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describeBattery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
    def getRange(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
