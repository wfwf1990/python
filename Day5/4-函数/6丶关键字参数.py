# Author: wangfang

'''
概念：允许函数调用时参数的顺序与定义时不一致
'''
def myPrint(str,age):
    print(str,age)

myPrint(age = 18,str = "tom is good man")