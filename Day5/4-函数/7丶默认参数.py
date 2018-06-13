# Author: wangfang
'''
概念：调用函数时,如果没有传递参数，则使用默认参数
'''
#注意：默认参数,把默认参数放到最后
def myPrint(str = "tom",age = 18):
    print(str,age)

myPrint()
myPrint("jack",19)
myPrint("alex")
