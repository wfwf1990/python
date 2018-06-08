num1 = 10
num2 = num1
#连续定义多个变量
num3 = num4 = num5 = 1
print(num3,num4,num5)

#交互式赋值定义变量
num6,num7 = 6, 7
print(num6,num7)


'''
浮点数:浮点数由整数部分与小数部分组成,浮点数运算可能会有四舍五入的误差
'''
f1 = 1.1
f2 = 2.2
print(f1 + f2)

'''
数字类型转换
'''
print(int(1.9))
print(float(1))
#字符串转换如果有其它字符会报错
print(int("123"))
print(float("123"))
#print(int("abc"))

#+-号只有作为正负号才有意义
print(int("+123"))
print(int("-123"))
#print(int("12-3"))




#数字的函数功能

#返回数字的绝对值
a1 = -10
a2 = abs(a1)
print(a2)

#比较两个数的大小,结果返回1丶-1丶0
a3 = 99
a4 = 99
print((a3>a4)-(a3<a4))

#返回给定参数的最大值
print(max(a3,a4))
print(max(1,2,3,4,5,6))
#返回给定参数的最小值
print(min(a3,a4))

#求x的y次方 2^5
print(pow(2,5))

#round(x[,n]),返回浮点数x的四舍五入的值,如果给出n值,则代表舍入到小数点后n位
print(round(3.456))             #整数的四舍五入
print(round(3.556, 2))          #保留两位小数


#随机数
import random
#从序列的元素中挑选一个元素
print(random.choice([1,3,4,56]))    #随机从列表中拿出一个数字
print(random.choice(range(5)))      #range(5) == [0,1,2,3,4]
print(random.choice("hello"))       #"hello" == ["h","e","l","l","o"]

#产生一个1~100之间的随机数
r1 = random.choice(range(100)) + 1
print(r1)


#从指定范围内,按指定的基数递增的集合中选取一个随机数
#random.randrange([start,] stop[,step])
#start --指定范围的开始值,包含在范围内
#stop --指定范围内的结束值,不包含在范围内
#step --指定的递增基数
print(random.randrange(1,100,2))

#从0-99选取一个随机数
print(random.randrange(100))

#随机生成[0,1)之间的一个数(浮点数)
print(random.random())

#将序列的所有元素随机排序
list = [1,2,3,4,5]
random.shuffle(list)
print(list)

#随机产生一个实数（小数或整数）,它在[3,9]范围内
print(random.uniform(3,9))