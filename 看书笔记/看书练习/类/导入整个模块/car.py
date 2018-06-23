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


