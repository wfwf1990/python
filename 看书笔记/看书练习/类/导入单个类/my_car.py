# Author: wangfang
#导入单个类

from car import Car

my_new_car = Car("audi","A6","2018")
print(my_new_car.getDescriptiveName())

my_new_car.odometer_reading = 23
my_new_car.getOdometerReading()



