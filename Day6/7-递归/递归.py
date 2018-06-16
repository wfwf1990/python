# Author: wangfang
'''
递归调用：一个函数，调用了自身,称为递归调用
递归函数：一个会调用自身的函数称为递归函数

凡是循环能干的事,递归都能干

'''

def sum1(n):
    if n == 1:
        return 1
    else:
        return sum1(n-1) + n
print(sum1(3))