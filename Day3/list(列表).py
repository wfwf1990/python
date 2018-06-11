'''
列表：
    本质：是一种有序的集合


'''

#（1）创建列表
'''
格式：列表名 = [列表选项1,列表选项2,....列表选项n]
'''

#创建一个空列表
list1 = []
print(list1)

#创建带有元素的列表
list2 = [10,220]
print(list2)
#注意：列表中的元素数据可以是不同类型
list3 = [1,2,"tom",True,None]
print(list3)

#（2）列表元素的访问
#取值   格式：列表名[下标]
list4 = [1,2,3,4,5]
print(list4[2])

#替换
list4[2] = 300
print(list4)


#（3）列表操作
#1）列表组合
list5 = [1,2,3]
list6 = [4,5,6]
list7 = list5 + list6
print(list7)

#2）列表的重复
list8 = [1,2,3]
print(list8 * 3)

#3）判断元素是否在列表中
list9 = [1,2,3,4,5]
print(3 in list9)
print(6 in list9)
print(6 not in list9)

#4）列表截取
list10 = [1,2,3,4,5,6,7]
print(list10[2:5])
print(list10[:5])
print(list10[5:])

#5）二维列表,列表作为列表的元素
list11 = [[1,2,3,4,5],[6,7,8,9,10]]
print(list11[0][3])

#（4）列表方法
'''
添加
    append 
    extend 
删除
    pop()
    remove()
    clear()
'''
#1）append()   在列表的末尾添加新的元素
list12 = [1,2,3,4,5]
list12.append(6)
list12.append([7,8,9])
print(list12)

#2）extend()  在末尾一次性追加另一个列中的多个值
list13 = [1,2,3,4,5]
list13.extend([6,7,8])
print(list13)

#3）insert()  在下标处添加一个元素,不覆盖原数据,原数据向后顺延
list14 = [1,2,3,4,5]
list14.insert(1,100)
list14.insert(2,[200,300])
print(list14)

#4）pop(x=list[-1])  移除列表中指定下标处的元素(默认移除最后一个元素),并返回删除的数据
list15 = [1,2,3,4,5]
list15.pop()
list15.pop(2)
print(list15.pop(2))
print(list15)

#5）remove()  移除列表中的某个元素第一个匹配的结果
list16 = [1,2,3,4,5,4]
list16.remove(4)
print(list16)

#6）clear()  清除列表中所有的数据
list17 = [1,2,3,4,5,4]
list17.clear()
print(list17)

#7）index()  从列表中找出某个值第一个匹配的索引值
list18 = [1,2,3,4,5,3]
index18 = list18.index(3)
index19 = list18.index(3,1,5)    #圈定范围
print(index18)

#8）len() 列表中元素个数
list19 = [1,2,3,4,5,3]
print(len(list19))

#9）max() 获取列表中的最大值   min() 获取列表中的最小值
list20 = [1,2,3,4,5]
print(max(list20))
print(min(list20))

#10）count()  查看元素在列表中出现的次数
list21 = [1,2,3,3,5,4,3]
print(list21.count(3))

#删除列表中所有的3元素

index = 0
all = list21.count(3)
while index < all:
    list21.remove(3)
    index += 1
print(list21)

#11）reverse() 倒序
list22 = [1,2,3,4,5]
list22.reverse()
print(list22)

#12）sort()  升序
list23 = [2,1,3,5,4]
list23.sort()
print(list23)

#13） 浅拷贝和深拷贝

# 浅拷贝
list24 = [1,2,3,4,5]
list25 = list24
list25[0] = 100
print(list25,list24)
print(id(list25),id(list24))

#深拷贝
list26 = [1,2,3,4,5]
list27 = list26.copy()
list27[0] = 200
print(list26,list27)
print(id(list26),id(list27))


#14）list() 将元组转换成列表
list28 = list((1,2,3,4))
print(list28)

