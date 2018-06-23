# Author: wangfang
''''''
'''
self代表类的实例，而非类
哪个对象调用方法,那么该方法中的self就代表哪个对象
self.__class__ 代表类名  不重要
'''

class Person(object):
    def run(self):
        print("run")
    def eat(self,food):
        print("eat " + food)
    def say(self):
        print("my name is %s,I am %d years old!" %(self.name,self.age))
        print(self.__class__)
    def __init__(self,name,age):
        self.name = name
        self.age = age

per1 = Person("tom",18)
per1.say()

per2 = Person("jack",19)
per2.say()

