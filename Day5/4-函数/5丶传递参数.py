# Author: wangfang
'''
值传递：传递的不可变类型
字符串,元祖,数字是不可变的
'''
def fun1(num):
    num = 10
temp = 20
fun1(temp)
print(temp)


'''
引用传递：传递的可变类型
list,dict,set是可变的
'''
def fun2(list):
    list[0] = 100

list = [1,100,200]
fun2(list)
print(list)