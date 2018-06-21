class Person(object):
    def __init__(self,money = 100,name = "",age = 18):
        self.name = name
        self.age = age
        self.__money = money
    def run(self):
        print("run")
        print(per1.__money)
    def eat(self,food):
        print("eat " + food)
    def __str__(self):
        return "%s-%d" %(self.name,self.age)
    #通过内部的方法，取修改私有属性
    #通过自定义的方法实现对私有属性的赋值与取值
    def setMoney(self,money):
        self.__money = money
    def getMoney(self):
       return self.__money
per1 = Person()
per1.age = 20
print(per1.age)

'''
如果要让内部的属性不被外部直接访问,在属性前价格两个下划线(__)，在python中如果在属性前加
两个下划线,那么这个属性就变成了私有属性
'''

per1.setMoney(10)               #设置私有属性
print(per1.getMoney())          #获取私有属性
'''
不能直接访问per.__money是因为python解释器把__money变成了_Person__money
仍然可以用__Person__money取访问，但是强烈建议不要这么干
'''
per1._Person__money = 1
print(per1.getMoney())



#在python中 __xxx__ 属于特殊变量，可以直接访问

#在python中，_xxx    这样的变量也可以在外部直接访问，但是按照约定的规则，当我们看到这样的变量时,意思是"虽然我可以被访问，但是请把我视为私有变量"

class D123(object):
    def __init__(self):
        name = ""
    def Shoot(self):
        if self.b