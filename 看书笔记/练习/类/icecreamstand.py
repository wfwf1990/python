# Author: wangfang

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0          #设置吃饭人数，初始值为0
    def describe_restaurant(self):
        print("restaurant's name is %s, and cuisine_type is %s" %(self.restaurant_name,self.cuisine_type))
    def open_restaurant(self):
        print("The restaurant is open")
    def getServedNumber(self):              #获取吃饭人数方法
        print("现在吃饭人数是%d" %self.number_served)
    def setNumberServed(self,num):          #设置吃饭人数方法
        if num >=0:
            self.number_served = num
        else:
            print("吃饭人数不能为负数")
    def incrementNumberServed(self,num):    #设置吃饭人数递增方法
        if num >= 0:
            self.number_served += num
        else:
            print("吃饭递增人数不能为0")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name,cuisine_type)
        self.flavors = ["甜","奶油味"]
    def getIceCream(self):
        for icecream in self.flavors:
            print("This is a %s ice cream!" %icecream)

icecream = IceCreamStand("冰淇淋店铺","冷饮")
icecream.describe_restaurant()
icecream.getIceCream()