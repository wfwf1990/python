# Author: wangfang

'''
概率：不适用def这样的语句定义函数,使用lambda来创建匿名函数
特点：
    1丶lambda只是一个表达式,函数体比def简单
    2丶lambda的主体是一个表达式，而不是代码块，仅仅只能在lambda表达式中封装简单的表达式
    3丶
格式：
    lambda 参数1,参数2,参数...参数N:expression

'''
sum = lambda num1,num2:num1 + num2
print(sum(1,2))
