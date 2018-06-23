# Author: wangfang

class Person(object):
    def run(self):
        print("run")
    def eat(self,food):
        print("eat " + food)
    def openDoor(self):
        print("opendoor")
    def fillEle(self):
        print("fill")
    def closeDoor(self):
        print(close)
    def __init__(self,name,age):
        #定义属性
        self.name = name
        self.age = age


'''
构造函数：__init__() 在使用类创建对象的时候自动调用
注意：如果不显示的写出构造函数，默认会自动添加一个空的构造函数
'''
#创建对象传入的列表参数就是给类中的构建函数传参
#self 代表当前创建的对象
per1 = Person("tom",19)
print(per1.name,per1.age)

per2 = Person("jack",20)
print(per2.name,per2.age)