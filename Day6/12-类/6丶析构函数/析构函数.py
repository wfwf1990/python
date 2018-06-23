# Author: wangfang
''''''
'''
析构函数： __del__()  释放对象的时候执行
'''

class Person(object):
    def run(self):
        print("run")
    def eat(self,food):
        print("eat " + food)
    def say(self):
        print("my name is %s,I am %d years old!" %(self.name,self.age))
        print(self.__class__)
    def __init__(self,name = "",age = 18):
        self.name = name
        self.age = age
    def __del__(self):
        print("这是析构函数")

per1 = Person()
per1.eat("apple")

del per1

#对象被释放就无法访问了
#print(per1.name)


#函数中创建对象,会在函数结束时自动释放对象，这样会节省内存空间的浪费
def func1():
    per2 = Person()
func1()