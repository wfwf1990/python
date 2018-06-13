'''
set:类似dict,是一组key的集合,不存储value
本质：无序和无重复元素的集合
'''

#（1）创建
#创建set需要一个list或者tuple或者dict作为输入集合
#重复元素在set中自动被过滤
set1 = set([1,2,3,3,3,4,5,6])
set2 = set((1,2,3,3))
set3 = set({1:"tom",2:"jack"})
print(set1)
print(set2)
print(set3)

#（2）添加
set4 = set([1,2,3,3,3,4,5,6])
set4.add(7)
set4.add(6)  #可以添加重复的，但是不会有效果
#set4.add([1,2,3])   #set的元素不能是列表,因为列表是可变的
set4.add((1,2,3))   #set的元素可以是元组,因为元组不可变
#set4.add({1:"3"})  #set的元素不能是字典,因为字典是可变的
print(set4)

#（3）插入
#插入整个list,tuple,字符串打碎插入
set5 = set([1,2,3,3,3,4,5,6])
set5.update([7,8,9])
set5.update((10,11))
set5.update("tom")
print(set5)

#（4）删除
set6 = set([1,2,3,3,3,4,5,6])
set6.remove(3)
print(set6)

#（5）遍历
set7 = set([1,2,3,3,3,4,5,6])
for i in set7:
    print(i)
#set没有索引,set[index]  会报错

for index,data in enumerate(set7):
    print(index,data)

#（6）交集
set8 = set([1,2,3])
set9 = set([2,3,4])
#交集：两个集合的共同部分
a1 = set8 & set9
print(a1)
print(type(a1))

#并集：两个集合合并
a2 = set8 | set9
print(a2)
print(type(a2))
