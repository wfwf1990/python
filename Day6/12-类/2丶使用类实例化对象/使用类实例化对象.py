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
'''
实例化对象:创建对象
格式：对象名 = 类名（参数列表）
注意：没有参数,小括号也不能省略
'''
per1 = Person()
print(per1)
per2 = Person()
print(per2)