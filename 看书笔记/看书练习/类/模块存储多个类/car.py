class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def getDescriptiveName(self):                 #返回描述性信息
        long_name = str(self.year) + " " + self.make + " "+ self.model
        return long_name.title()
    def getOdometerReading(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")
    #通过方法接受一个里程值,并将其存储到self.odometer_reading中
    def updateOdometer(self,mileage):
        #禁止将里程数往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can not roll back an odometer")
    def increment_odometer(self,miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("you can not roll back an odometer")

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
