# Author: wangfang
from car import Car
from electric_car import ElectricCar,Battery

my_bwm = Car("bwm","x3",2018)
print(my_bwm.getDescriptiveName())

my_tesla = ElectricCar("tesla","model S","2017")
print(my_tesla.getDescriptiveName())