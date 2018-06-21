'''
重写：将函数重写定义写一遍
__str__() ：在调用print打印对象时自动调用，是一个描述对象的方法
__repr__() ：是给机器用的，在Python解释器里面直接敲对象名回车后调用的方法
注意：在没有str时，且有repr，str = repr
'''


class Person(object):
    def __init__(self,name = "",age = 18):
        self.name = name
        self.age = age
    def run(self):
        print("run")
    def eat(self,food):
        print("eat " + food)
    def __str__(self):
        return "%s-%d" %(self.name,self.age)

per1 = Person()
print(per1.name,per1.age)
print(per1) #相当于print(per1.__str__())


#优点：当一个对象的属性值很多，并且都需要打印，重写了__str__方法后，简化了代码
