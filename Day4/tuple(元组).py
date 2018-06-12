
'''
tuple
    本质：是一种有序集合
特点：
    与列表非常相似
    一旦初始化就不能修改
    使用小括号
'''
#创建元组
#格式：元组名 =  （元组元素1,元组元素2,....元组元素n）





#元组元素的访问
#格式：元组名[下标]
tuple4 = (1,2,3,4,5)
print(tuple4[0])
print(tuple4[-1])           #获取最后一个元素


#修改元组
tuple5 = (1,2,3,4,5,[1,2,3,4])
tuple5[-1][1] = 500     #元组元素不能变,元组中的元素如果是列表,列表中的元素是可以变
print(tuple5)

#修改元组
tuple6 = (1,2,3,4,5)
del tuple6

#元组操作
tuple7 = (1,2,3)
tuple8 = (4,5,6)
print(tuple7 + tuple8)


#元组重复
tuple9 = (1,2,3)
print(tuple9 * 3)

#判断元素是否在元组中
tuple10 = (1,2,3)
print(1 in tuple10)

#元组的截取
#格式：元组名[开始下标:结束下标]
tuple11 = (1,2,3,4,5,6,7,8,9)
print(tuple11[3:7])
print(tuple11[3:])
print(tuple11[:7])


#二维元组:元素为一维元组的元组
tuple13 = ((1,2,3),(4,5,6),(7,8,9))
print(tuple13[-1][1])

#元组方法

#len()    返回元组中元素的个数
tuple14 = (1,2,3,4,5)
print(len(tuple14))

#max() 返回元组中的最大值
#min()
print(max(1,2,3,4,5))
print(min(1,2,3,4,5))

#将列表转换成元组
list = [1,2,3,4,5]
tuple15 = tuple(list)
print(tuple15)

#元组的元素遍历
tuple16 = (1,2,3,4,5)
for i in tuple16:
    print(i)