# Author: wangfang
'''
概念：能处理比定义时更多的参数

'''
#加了*号的变量存放所有未命名的参数，如果在函数没有指定参数,它就是一个空元祖

def func(name,*args):
    print(name)
    for i in args:
        print(i)
func("tom","jack","alex")

def mySum(*num):
    sum = 0
    for i in num:
        sum += i
    return sum
ret = mySum(1,2,3)
print(ret)

#** 代表key-value的参数字典，和*所代表的意义类似
#返回字典

def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))
func2(x=1,y=2)