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
restaurant = Restaurant("KFC","fastFood")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.getServedNumber()
restaurant.setNumberServed(10)
restaurant.getServedNumber()
restaurant.incrementNumberServed(20)
restaurant.getServedNumber()
restaurant.incrementNumberServed(-10)
restaurant.getServedNumber()
'''
restaurant_md = Restaurant("麦当劳","快餐")
restaurant_sb = Restaurant("星巴克","咖啡")
restaurant_dicos = Restaurant("德克士","快餐")

restaurant_md.describe_restaurant()
restaurant_sb.describe_restaurant()
restaurant_dicos.describe_restaurant()
'''
