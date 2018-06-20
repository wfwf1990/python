# Author: wangfang
class Person(object):
    name = ""
    age = 0
    height = 0
    weight = 0

    def run(self):
        print("run")
    def eat(self,food):
        print("eat" + food)
    def openDoor(self):
        print("opendoor")
    def fillEle(self):
        print("fill")
    def closeDoor(self):
        print(close)
per1 = Person()

'''
访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 赋值
'''
per1.name = "tom"
per1.age = 18
per1.height = 175
per1.weight = 80
print(per1.name,per1.age)



