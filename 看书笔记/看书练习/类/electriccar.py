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


#创建子类：子类继承父类的属性和方法
'''
class ElectricCar(Car):             #定义电动汽车子类,其中括号为父类的名称
    def __init__(self,make,modle,year):     #接受创建Car实例所需的信息
        super(ElectricCar, self).__init__(make,modle,year)   #super特殊函数,将父类和子类关联起来

my_new_car = ElectricCar("tesla","model S",2016)            #子类继承了父类的属性和方法
print(my_new_car.getDescriptiveName())                
'''
#
#创建子类的特有属性和方法
class ElectricCar(Car):
    def __init__(self,make,modle,year):
        super(ElectricCar, self).__init__(make,modle,year)
        self.battery_size = 70              #创建电动汽车电瓶的容量
    def describeBattery(self):              #打印一条描述电瓶容量的方法
        print("This car has a " + str(self.battery_size) + "-KWh battery")
my_tesla = ElectricCar("tesla","model S",2016)
print(my_tesla.getDescriptiveName())
my_tesla.describeBattery()